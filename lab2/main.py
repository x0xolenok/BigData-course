import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine

# 1. Load the Wine dataset from sklearn
wine_data = load_wine()
df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)

# 2. Check for missing values
if df.isnull().sum().any():
    df = df.fillna(df.mean())  # Fill missing values with the mean

# 3. Standardize the data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)

# 4. Perform PCA
pca = PCA()
pca.fit(df_scaled)

# 5. Calculate cumulative variance to determine the number of components
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance_ratio)

# 6. Create a scree plot to select the number of components
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance_ratio) + 1), cumulative_variance, marker='o', linestyle='--')
plt.title('Cumulative Explained Variance')
plt.xlabel('Number of Principal Components')
plt.ylabel('Cumulative Variance Explained')
plt.grid(True)
plt.show()

# 7. Select the optimal number of components (e.g., 90% variance)
optimal_components = np.argmax(cumulative_variance >= 0.90) + 1
print(f'Optimal number of components: {optimal_components}')

# 8. Transform data using the optimal number of components
pca_optimal = PCA(n_components=optimal_components)
df_pca = pca_optimal.fit_transform(df_scaled)

# 9. Visualization in reduced dimensionality (e.g., 2 components)
if optimal_components >= 2:
    plt.figure(figsize=(8, 6))
    plt.scatter(df_pca[:, 0], df_pca[:, 1], alpha=0.5, c=wine_data.target, cmap='viridis')
    plt.title('PCA: 2 Components')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(label='Wine Class')
    plt.show()
