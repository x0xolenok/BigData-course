# Advanced clustering methods
1. Select one of the following methods (hierarchical or spectral)
2. Get acquainted with the theory
3. Use the Python libraries 
4. Investigate the advantages and disadvantages of the algorithm in comparison with k-means
5. Focus on the theoretical part

# Report
# 1. The selected method: Hierarchical clustering method
The hierarchical clustering method was chosen for this task. This method is a popular approach for dividing data into clusters, which is based on calculating the distances between points and gradually combining the points into groups. In the hierarchical method, clusters are formed by iteratively combining the closest points or groups of points until the desired number of clusters remains.

# 2. Python libraries used
The following Python libraries were used for this task:
- ```NumPy``` for calculating and working with arrays.
- ```Matplotlib``` for visualising clustering on a graph.
- ```scikit-learn (sklearn)``` for generating synthetic data in the form of two crescents with the ```make_moons``` function.
- ```silhouette_score``` from ```sklearn.metrics``` to evaluate the quality of clustering based on the average silhouette coefficient.

# 3. Advantages and disadvantages of the hierarchical method compared to the k-means method

# Advantages of hierarchical clustering:
- Hierarchical clustering allows you to identify clusters with complex shapes, while the k-means method works well only with round clusters.
- Does not require pre-selection of the number of clusters, although this number can be selected at a certain stage of the dendrogram.
- It can build a dendrogram that allows you to examine the relationships between points and clusters in detail.
# Disadvantages of hierarchical clustering:
- The hierarchical method is computationally intensive, especially for large datasets, unlike k-means, which is faster and less resource-intensive.
- It is difficult to integrate in case of dynamic data updates, while the k-means method can be easily re-executed for new data.

# Advantages of the k-means method:
- Faster to run, especially for large datasets.
- Easier to implement and has lower computational requirements, making it effective for clustering large amounts of data.
# Disadvantages of k-means:
- Requires a predetermined number of clusters.
- Not suitable for detecting clusters with complex shapes, as it assumes that all clusters are spherical.

# Result: 
- The graph shows two groups of points illustrating successful clustering into two clusters using the hierarchical method.

![image](https://github.com/user-attachments/assets/d4c941b1-5f60-4f27-984d-b0c6ba50374e)

```bash
Average silhouette coefficient: 0.44
Algorithm execution time: 0.2889 seconds.
```
