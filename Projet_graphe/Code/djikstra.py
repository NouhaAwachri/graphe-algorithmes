from math import inf
def djikstra(graph, start_vertex):
    n = len(graph)
    distance = [float('inf')] * n #Initialize an array distance to store the shortest distances from the source vertex to each vertex. Initialize all distances to infinity.
    visited = [False] * n #nitialize an array visited to keep track of visited vertices. Initially, no vertex is visited.
    distance[start_vertex - 1] = 0 # Set the distance of the source vertex to 0, as the distance from the source to itself is 0.

    for _ in range(n):
        min_distance = float('inf')
        min_vertex = -1 #sommet 

        # Find the vertex with the minimum distance
        for v in range(n):
            if not visited[v] and distance[v] < min_distance:
                min_distance = distance[v]
                min_vertex = v

        # Mark the selected vertex as visited
        visited[min_vertex] = True

        # Update the distances to neighbors of the selected vertex
        for neighbor in range(n):
            if not visited[neighbor] and graph[min_vertex][neighbor] != 0 \
                    and distance[min_vertex] + graph[min_vertex][neighbor] < distance[neighbor]:
                distance[neighbor] = distance[min_vertex] + graph[min_vertex][neighbor]

    return distance