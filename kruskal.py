
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(num_vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    mst = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))

    return mst

num_vertices = 4
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]


minimum_spanning_tree = kruskal(num_vertices, edges)
print("Minimum Spanning Tree:", minimum_spanning_tree)

'''


def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # Path compression
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(num_vertices, edges):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    parent = list(range(num_vertices))
    rank = [0] * num_vertices
    mst = []

    for u, v, weight in edges:
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            mst.append((u, v, weight))

    return mst

# Input section
num_vertices = int(input("Enter number of vertices: "))
num_edges = int(input("Enter number of edges: "))
edges = []

for i in range(num_edges):
    print(f"Edge {i + 1}:")
    u = int(input("  Enter start vertex (0-based index): "))
    v = int(input("  Enter end vertex (0-based index): "))
    w = int(input("  Enter weight: "))
    edges.append((u, v, w))

# Running Kruskal's algorithm
minimum_spanning_tree = kruskal(num_vertices, edges)

# Output result
print("\nMinimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(f"{u} - {v} : {weight}")

'''
