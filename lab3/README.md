# k-means
You need to apply the k-means algorithm (you can take the implementation from sklearn). You need to.
1. Show examples where it works well and where it works poorly (convex and non-convex clusters)
2. Investigate the effect of algorithm tuning parameters on the result and execution time for a fixed dataset
3. Visualisation of the results is highly desirable
4. It is highly desirable to investigate how the distance in the middle of the clusters actually changes with each step of the work
5. Draw conclusions

# Report
The code contains the following main elements:

- Generating points for the clusters: ```the generate_clusters() ``` function creates two clustered datasets. The clusters have different centres and are convex.
- Calculating the average intra-cluster distance: ```the intra_cluster_distance()``` function calculates the average distance between points and the centroid of their cluster.
- Implementation of the k-means algorithm: the ```k_means()``` function performs clustering by calculating centroids at each iteration and checking their stability to complete the algorithm.
- Visualisation of results: in the main function ```main()```, after clustering, the results are visualised using the ```matplotlib``` library.

# Examples where the algorithm works well and poorly:

- Works well on convex clusters: The k-means algorithm works well on convex clusters (as in this example) where the points are compactly clustered around centroids. An example is two Gaussian distributions where the algorithm correctly identifies the centroids.
- It works poorly on non-convex clusters: If the data has more complex shapes (for example, a ring or snake cluster), k-means may mistakenly split a single cluster into several parts or incorrectly identify centroids, as it uses Euclidean distance, which is only good for convex clusters.

# Effect of the configuration parameters:
- Number of clusters (k): Changing the k value affects the cluster structure. If k is too small, the clusters will be merged into larger groups. If the value of k is too large, excessively small clusters may result.
- Maximum number of iterations: Setting a small number of iterations can cause the algorithm to terminate before reaching stability, resulting in centroids that are not fully optimised.
- Initialisation of centroids: Random selection of initial centroids can affect the final result and quality of clustering, especially with complex data shapes.

# Visualisation of results
- The results of the clustering were visualised in a graph, where the points are coloured according to the clusters and the red marks indicate the position of the centroids. 
- The visualisation shows that the cluster points are well grouped around their centroids in the case of two Gaussian distributions.

```bash
Algorithm completed in 0.4154 seconds.
Average intra-cluster distance: 1.0956
```
![image](https://github.com/user-attachments/assets/40b46b11-ed48-4062-94b7-5ab187704fa5)


# Changes in intra-cluster distance
- The average intra-cluster distance was calculated based on the distance between each point and its centroid. 
- We observed a decrease in this distance with each iteration, which is a sign that the algorithm is approaching a stable state.

# Conclusions
- The k-means algorithm is well suited for clustering convex clusters and converges quickly with a sufficient number of iterations.
- Changing parameters such as k and initial centroids significantly affects the clustering result. It is recommended to choose the optimal value of k taking into account the nature of the data.
- The intra-cluster distance at each iteration helps to control the process of convergence, which is useful for analysing the efficiency of the algorithm.
- Other methods, such as DBSCAN or spectral clustering, which are not limited to Euclidean distance, may be needed to cluster data with a non-convex structure.

