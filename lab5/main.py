import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = datasets.load_iris()
X = data.data
y = data.target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Function to train and evaluate the model
def train_and_evaluate_svm(C, kernel, gamma='scale'):
    model = SVC(C=C, kernel=kernel, gamma=gamma)  # Create SVM model with specified parameters
    model.fit(X_train, y_train)  # Train the model on the training data
    y_pred = model.predict(X_test)  # Make predictions on the test data
    accuracy = accuracy_score(y_test, y_pred)  # Calculate accuracy
    cm = confusion_matrix(y_test, y_pred)  # Calculate confusion matrix
    return accuracy, cm

# Parameters for investigation
C_values = [0.1, 1, 10]  # Different values of C for testing
kernels = ['linear', 'rbf', 'poly']  # Kernels to investigate
gamma_values = ['scale', 'auto']  # Gamma values for non-linear kernels

# Investigate the impact of parameters
results = {}
for C in C_values:
    for kernel in kernels:
        for gamma in gamma_values:
            accuracy, cm = train_and_evaluate_svm(C, kernel, gamma)
            results[(C, kernel, gamma)] = (accuracy, cm)
            print(f"C={C}, kernel={kernel}, gamma={gamma} -> Accuracy: {accuracy:.2f}")

# Visualization of results (example for one case)
C, kernel, gamma = 1, 'rbf', 'scale'  # Selected parameters for visualization
_, cm = results[(C, kernel, gamma)]  # Get confusion matrix for the specified parameters
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")  # Plot confusion matrix heatmap
plt.title(f'Confusion Matrix (C={C}, kernel={kernel}, gamma={gamma})')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
