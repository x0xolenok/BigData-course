import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import pairwise_distances_argmin
import time


# Function to generate points with convex and non-convex clusters
def generate_clusters(num_points=500):
    # Create two groups of points for convex clusters
    cluster_1 = np.random.normal(loc=(-5, -5), scale=1, size=(num_points // 2, 2))
    cluster_2 = np.random.normal(loc=(5, 5), scale=1, size=(num_points // 2, 2))

    # Combine into a general dataset
    points = np.vstack([cluster_1, cluster_2])
    return points


# Function to compute the average intra-cluster distance
def intra_cluster_distance(points, labels, centroids):
    total_distance = 0
    count = 0
    for i, point in enumerate(points):
        centroid = centroids[labels[i]]
        total_distance += np.linalg.norm(point - centroid)
        count += 1
    return total_distance / count


# Main k-means algorithm
def k_means(points, k, max_iterations=100):
    # Initialize centroids with random points from the dataset
    centroids = points[np.random.choice(points.shape[0], k, replace=False)]
    for i in range(max_iterations):
        # Assign each point to the nearest centroid
        labels = pairwise_distances_argmin(points, centroids)

        # Update centroids
        new_centroids = np.array([points[labels == j].mean(axis=0) for j in range(k)])

        # Check if centroids are unchanged
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids

    return labels, centroids


# Main function to execute all tasks
def main():
    k = 3
    max_iterations = 100
    points = generate_clusters(500)

    # Measure execution time
    start_time = time.time()
    labels, centroids = k_means(points, k, max_iterations)
    end_time = time.time()
    print(f"Algorithm completed in {end_time - start_time:.4f} seconds.")

    # Visualize the results
    plt.scatter(points[:, 0], points[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=50)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
    plt.title("k-means Clustering Results")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Compute intra-cluster distance
    avg_intra_distance = intra_cluster_distance(points, labels, centroids)
    print(f"Average intra-cluster distance: {avg_intra_distance:.4f}")


if __name__ == "__main__":
    main()
