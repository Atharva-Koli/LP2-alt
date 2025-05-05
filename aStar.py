import heapq

def astar(start, goal, graph, heuristic):
    openlist = []
    heapq.heappush(openlist, (0 + heuristic[start], 0, start, [start]))
    visited = set()

    while openlist:
        f, g, current, path = heapq.heappop(openlist)

        if current == goal:
            print("Total path:", path)
            print("Total cost:", g)
            return path

        if current in visited:
            continue
        visited.add(current)

        for neighbour, cost in graph.get(current, []):
            if neighbour not in visited:
                heapq.heappush(openlist, (g + cost + heuristic[neighbour], g + cost, neighbour, path + [neighbour]))

    print("Path doesn't exist")
    return None

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

astar('A', 'G', graph, heuristic)



import heapq

def a_star_search(start, goal, graph, heuristic):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], 0, start, [start]))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current == goal:
            print("Total path:", path)
            print("Total cost:", g)
            return

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(open_list, (g + cost + heuristic[neighbor], g + cost, neighbor, path + [neighbor]))

    print("Path doesn't exist")

# Take user input
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors (format: B 2 C 3): ").split()
    graph[node] = [(neighbors[i], int(neighbors[i+1])) for i in range(0, len(neighbors), 2)]

heuristic = {}
for node in graph:
    heuristic[node] = int(input(f"Enter heuristic value for {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

a_star_search(start, goal, graph, heuristic)
