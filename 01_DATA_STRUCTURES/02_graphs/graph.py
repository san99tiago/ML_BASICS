# BASIC GRAPH DATA STRUCTURE WITH ADJACENCY LISTS
# Santiago Garcia Arango, July 2020

class Vertex:
    def __init__(self, name):
        self.name = name
        # List of tuples [(Vertex Object, distance)]
        self.neighbors = []

    def add_neighbor(self, vertex_neighbor, distance):
        # Check that the neighbor vertex is NOT already in neighbors
        if vertex_neighbor not in self.neighbors:
            self.neighbors.append((vertex_neighbor, distance))
            self.neighbors.sort(key=lambda n: n[0].name)


    def show_neighbors(self):
        print("[", end="")
        for n in range(len(self.neighbors)):
            print(self.neighbors[n][0].name, end=": ")
            print(self.neighbors[n][1], end=",")
        print("]")

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, new_vertex):
        is_vertex = isinstance(new_vertex, Vertex)
        is_not_in_graph = new_vertex.name not in self.vertices
        if is_vertex and is_not_in_graph:
            self.vertices[new_vertex.name] = new_vertex
            return True
        else:
            return False

    def add_edge(self, vertex_1, vertex_2, distance):
        name_1 = vertex_1.name
        name_2 = vertex_2.name
        are_in_graph = name_1 in self.vertices and name_2 in self.vertices
        if are_in_graph:
            self.vertices[name_1].add_neighbor(vertex_2, distance)
            self.vertices[name_2].add_neighbor(vertex_1, distance)
            return True
        else:
            return False

    def show_graph(self):
        for key in self.vertices.keys():
            print(key + " --> ", end="")
            self.vertices[key].show_neighbors()

# Check test in <test_graph.py> script
