graph ={
'A':['B','C'],
'B':['A','D'],
'C':['A','D'],
'D':['E'],
'E':['D']
}

result = {}
colors=['green','blue','red']

def is_safe(vertex,color):
	for neighbour in graph[vertex]:
		if neighbour in result and result[neighbour] == color:
			return False
	return True

def color_graph():
	for vertex in graph:
		for color in colors:
			if is_safe(vertex,color):
				result[vertex] = color
				break
color_graph()
for vertex in result:
    print(f"{vertex} --> {result[vertex]}")



graph = {}
result = {}
colors = ['green', 'blue', 'red']

# Input graph
n = int(input("Enter number of vertices: "))
for _ in range(n):
    vertex = input("Enter vertex: ")
    neighbours = input(f"Enter neighbours of {vertex} separated by space: ").split()
    graph[vertex] = neighbours

def is_safe(vertex, color):
    for neighbour in graph[vertex]:
        if neighbour in result and result[neighbour] == color:
            return False
    return True

def color_graph():
    for vertex in graph:
        for color in colors:
            if is_safe(vertex, color):
                result[vertex] = color
                break

color_graph()

print("\nVertex -> Assigned Color:")
for vertex in result:
    print(f"{vertex} --> {result[vertex]}")
