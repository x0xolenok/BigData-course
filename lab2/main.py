import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# 1. Завантажуємо датасет
df = pd.read_csv('E:\lab2\student-por.csv')

# 2. Вибір лише числових стовпців
df_numeric = df.select_dtypes(include=[np.number])

# 3. Перевірка на пропущені значення
if df_numeric.isnull().sum().any():
    df_numeric = df_numeric.fillna(df_numeric.mean())  # Заповнюємо пропущені значення середнім

# 4. Стандартизуємо дані
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

# 5. Виконуємо PCA
pca = PCA()
pca.fit(df_scaled)

# 6. Визначаємо кумулятивну дисперсію для вибору кількості компонент
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance_ratio)

# 7. Створюємо графік для вибору кількості компонент (scree plot)
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), cumulative_variance, marker='o', linestyle='--')
plt.title('Cumulative Explained Variance')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Variance Explained')
plt.grid(True)
plt.show()

# 8. Вибір оптимальної кількості компонент (наприклад, 90% дисперсії)
optimal_components = np.argmax(cumulative_variance >= 0.90) + 1
print(f'Optimal number of components: {optimal_components}')

# 9. Перетворення даних за допомогою оптимальної кількості компонент
pca_optimal = PCA(n_components=optimal_components)
df_pca = pca_optimal.fit_transform(df_scaled)

# 10. Візуалізація зменшеної розмірності (наприклад, 2 компоненти)
if optimal_components >= 2:
    plt.figure(figsize=(8, 6))
    plt.scatter(df_pca[:, 0], df_pca[:, 1], alpha=0.5, c=df['G1'], cmap='viridis')
    plt.title('PCA: 2 Components')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(label='G1 grade')
    plt.show()
