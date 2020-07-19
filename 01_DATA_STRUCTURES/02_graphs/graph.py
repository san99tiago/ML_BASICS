# BASIC GRAPH DATA STRUCTURE WITH ADJACENCY LISTS
# Santiago Garcia Arango, July 2020

class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, vertex_neighbor):
        # Check that the neighbor vertex is NOT already in neighbors
        if vertex_neighbor not in self.neighbors:
            self.neighbors.apprend(vertex_neighbor)


