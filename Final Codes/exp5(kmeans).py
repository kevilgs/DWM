# Get input
dims = int(input("Enter the number of dimensions (1 or 2): "))
if dims not in [1, 2]:
    print("Invalid number of dimensions. Exiting.")
    exit()

# Get points
points = []
for i in range(int(input("Enter the number of points: "))):
    if dims == 1:
        points.append([float(input(f"Enter value for point {i + 1}: "))])
    else:
        points.append([float(input(f"Enter x for point {i + 1}: ")),
                       float(input(f"Enter y for point {i + 1}: "))])

# Get centroids
centroids = []
for i in range(int(input("Enter the number of clusters (k): "))):
    if dims == 1:
        centroids.append([float(input(f"Enter value for centroid {i + 1}: "))])
    else:
        centroids.append([float(input(f"Enter x for centroid {i + 1}: ")),
                          float(input(f"Enter y for centroid {i + 1}: "))])

# K-means clustering function
def kmeans_clustering(points, centroids):
    while True:
        # Assign points to closest centroid
        clusters = [[] for _ in centroids]
        for point in points:
            # Find closest centroid using squared distance (faster than sqrt)
            distances = [sum((a - b) ** 2 for a, b in zip(point, c)) for c in centroids]
            clusters[distances.index(min(distances))].append(point)
        
        # Display clusters in the current iteration
        print("\nIteration:")
        for i, cluster in enumerate(clusters):
            print(f"Cluster {i + 1}: {cluster}")
        
        # Calculate new centroids
        new_centroids = []
        for cluster in clusters:
            if not cluster:  # Empty cluster
                new_centroids.append(centroids[len(new_centroids)])
                continue
            # Average of points in cluster
            new_centroids.append([sum(dim) / len(cluster) for dim in zip(*cluster)])
        
        # Display updated centroids in the current iteration
        print(f"Updated Centroids: {new_centroids}")
        
        # Check for convergence
        if new_centroids == centroids:
            print("\nCentroids have stabilized. Ending iterations.")
            break
        
        # Update centroids for next iteration
        centroids = new_centroids
    
    # Print final clusters and centroids outside the loop
    return clusters, centroids

# Run clustering and print results
clusters, final_centroids = kmeans_clustering(points, centroids)
print("\nFinal Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")
print(f"Final Centroids: {final_centroids}")

