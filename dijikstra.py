import heapq

def dijkstra(graph, start, destination):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    pq = [(0, start)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if u == destination:
            break
        
        for v, weight in graph[u].items():
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))
    
    path = []
    node = destination
    while node is not None:
        path.append(node)
        node = prev[node]
    path.reverse()
    
    return dist[destination], path


n = int(input("Enter number of nodes: "))
graph = {}


for _ in range(n):
    node = input("Enter node name: ")
    graph[node] = {}
    m = int(input(f"Enter number of neighbors for {node}: "))
    for _ in range(m):
        neighbor = input("  Enter neighbor: ")
        weight = int(input(f"  Enter weight to {neighbor}: "))
        graph[node][neighbor] = weight


start = input("Enter the start node: ")
destination = input("Enter the destination node: ")

if start in graph and destination in graph:
    shortest_distance, path = dijkstra(graph, start, destination)
    print(f"Shortest distance: {shortest_distance}")
    print(f"Path: {' -> '.join(path)}")
else:
    print("Invalid node(s) entered.")








Enter number of nodes: 4
Enter node name: A
Enter number of neighbors for A: 1
  Enter neighbor: C
  Enter weight to C: 4
Enter node name: B
Enter number of neighbors for B: 2
  Enter neighbor: A
  Enter weight to A: 1
  Enter neighbor: C
  Enter weight to C: 2
Enter node name: C
Enter number of neighbors for C: 3
  Enter neighbor: A
  Enter weight to A: 4
  Enter neighbor: B
  Enter weight to B: 2
  Enter neighbor: D
  Enter weight to D: 1
Enter node name: D
Enter number of neighbors for D: 1
  Enter neighbor: C
  Enter weight to C: 1
Enter the start node: A
Enter the destination node: D




