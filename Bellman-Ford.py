def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distances

graph = {
    's': [('t', 3), ('y', 5)],
    't': [('x', 6), ('y', 2)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

source = 's'
try:
    shortest_distances = bellman_ford(graph, source)
    print("Shortest distances from source node 's':")
    for node, distance in shortest_distances.items():
        print(f"Node {node}: {distance}")
except ValueError as e:
    print(e)
"""output"""
"""Shortest distances from source node 's':
Node s: 0
Node t: 3
Node y: 5
Node x: 9
Node z: 11"""    