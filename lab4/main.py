import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_moons, make_blobs
from sklearn.metrics import silhouette_score
import time

# Data generation
# "Moons" dataset for testing non-convex clusters
data_moons, _ = make_moons(n_samples=300, noise=0.1, random_state=42)

# Defining the number of clusters
n_clusters = 2

# Hierarchical clustering
start_time = time.time()
hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
labels_moons = hierarchical.fit_predict(data_moons)
end_time = time.time()

# Visualization of the results
plt.figure(figsize=(8, 6))
plt.scatter(data_moons[:, 0], data_moons[:, 1], c=labels_moons, cmap='viridis', marker='o', edgecolor='k')
plt.title(f"Hierarchical Clustering (n_clusters={n_clusters})")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Calculating and displaying the average silhouette coefficient
silhouette_avg = silhouette_score(data_moons, labels_moons)
print(f"Average silhouette coefficient: {silhouette_avg:.2f}")
print(f"Algorithm execution time: {end_time - start_time:.4f} seconds.")
