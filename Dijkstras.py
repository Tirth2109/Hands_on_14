import heapq

def dijkstra(graph, start):
    pq = []
    heapq.heappush(pq, (0, start))
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

graph = {
    's': [('t', 3), ('y', 5)],
    't': [('x', 6), ('y', 2)],
    'y': [('t', 1), ('x', 4), ('z', 6)],
    'x': [('z', 2)],
    'z': [('s', 3), ('x', 7)]
}

source = 's'
shortest_distances = dijkstra(graph, source)

print("Shortest distances from source node 's':")
for node, distance in shortest_distances.items():
    print(f"Node {node}: {distance}")
    
'''output'''
"""Shortest distances from source node 's':
Node s: 0
Node t: 3
Node y: 5
Node x: 9
Node z: 11"""