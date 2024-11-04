def calculate_pagerank(adjacency_matrix, num_iterations, teleportation_factor):
    size = len(adjacency_matrix)
    pagerank = []
    for i in range(size):
        pagerank.append(round(1.0 / size, 3))
        
    print("Iteration 0:", [round(p, 3) for p in pagerank], "\n")
    
    for iteration in range(num_iterations):
        new_pagerank = []
        
        for i in range(size):
            score = (1 - teleportation_factor)
            for j in range(size):
                if adjacency_matrix[j][i] > 0:
                    outbound_sum = sum(adjacency_matrix[j])
                    if outbound_sum > 0:
                        score += teleportation_factor * (pagerank[j] / outbound_sum)
            
            new_pagerank.append(round(score, 3))
            
        pagerank = new_pagerank
        print("Iteration", iteration + 1, ":", pagerank, "\n")
    
    print("Final PageRank values:")
    print(pagerank)
    
    best_page = pagerank.index(max(pagerank))
    print("\nThe most important page is: Page", chr(65 + best_page), "with a PageRank of", round(pagerank[best_page], 3), "\n")

    num_nodes = int(input("Enter the number of nodes in the graph: "))
    
    print("Enter the adjacency matrix row by row (use space to separate values):")
    adj_matrix = []
    for i in range(num_nodes):
        row = list(map(float, input().split()))
        adj_matrix.append(row)
    
    iterations = int(input("Enter the number of iterations: "))
    teleport = float(input("Enter the teleportation factor (between 0-1): "))
    
    calculate_pagerank(adj_matrix, iterations, teleport)

