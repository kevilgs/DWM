import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

def agglomerative_clustering(numbers, num_clusters):
    # Initialize each number as a separate cluster
    clusters = [[i] for i in range(len(numbers))]
    iteration = 1
    
    while len(clusters) > num_clusters:
        # Find closest pair of clusters
        min_distance = float('inf')
        merge_i = merge_j = 0
        
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                # Calculate minimum distance between clusters
                distance = min(abs(numbers[x] - numbers[y]) 
                             for x in clusters[i] 
                             for y in clusters[j])
                
                if distance < min_distance:
                    min_distance = distance
                    merge_i, merge_j = i, j
        
        # Merge clusters and print result
        clusters[merge_i].extend(clusters[merge_j])
        del clusters[merge_j]
        
        print(f"\nIteration {iteration}:")
        for idx, cluster in enumerate(clusters):
            print(f"Cluster {idx + 1}:", [int(numbers[i]) for i in cluster])
            
        iteration += 1
    
    return clusters

# Test data
numbers = [18, 22, 25, 27, 42, 43]
clusters = agglomerative_clustering(numbers, 1)

# Create and display dendrogram
plt.figure(figsize=(10, 7))
linked = linkage([[x] for x in numbers], method='single')
dendrogram(linked, labels=numbers)
plt.title("Dendrogram for Agglomerative Clustering")
plt.xlabel("Data Points")
plt.ylabel("Distance")
plt.show()