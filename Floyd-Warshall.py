def floyd_warshall_adj_list(graph):
    nodes = set(graph.keys())
    for node in graph:
        for neighbor, _ in graph[node]:
            nodes.add(neighbor)
    
    dist = {i: {j: float('inf') for j in nodes} for i in nodes}
    
    for node in nodes:
        dist[node][node] = 0
    
    for node in graph:
        for neighbor, weight in graph[node]:
            dist[node][neighbor] = weight
    
    for k in nodes:  
        for i in nodes:  
            for j in nodes: 
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


graph = {
    's': [('t', 3), ('y', 5)],
    't': [('x', 6), ('y', 2)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

shortest_paths = floyd_warshall_adj_list(graph)

print("Shortest path matrix:")
nodes = sorted(shortest_paths.keys())
print("    " + "   ".join(nodes))
for i in nodes:
    row = [f"{shortest_paths[i][j]:3}" if shortest_paths[i][j] != float('inf') else " ∞" for j in nodes]
    print(f"{i}: {'   '.join(row)}")
"""output"""
"""Shortest path matrix:
    s   t   x   y   z
s:   0     3     9     5    11
t:  11     0     6     2     8
x:   5     8     0    10     2
y:   9     1     4     0     6
z:   3     6     7     8     0"""