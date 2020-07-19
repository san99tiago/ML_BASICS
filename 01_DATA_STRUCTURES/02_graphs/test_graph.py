# TEST GRAPH SCRIPT WITH SIMPLE EXAMPLE
# Santiago Garcia Arango, July 2020

import graph

# Create Graph object
g1 = graph.Graph()

# Create all Vertex objects (that will be added to Graph)
S = graph.Vertex("S")
A = graph.Vertex("A")
B = graph.Vertex("B")
C = graph.Vertex("C")
D = graph.Vertex("D")
E = graph.Vertex("E")
G = graph.Vertex("G")

# Add all Vertex objects to the graph
g1.add_vertex(S)
g1.add_vertex(A)
g1.add_vertex(B)
g1.add_vertex(C)
g1.add_vertex(D)
g1.add_vertex(E)
g1.add_vertex(G)

g1.add_edge(S, A, 3)
g1.add_edge(S, B, 5)
g1.add_edge(A, B, 4)
g1.add_edge(B, C, 4)
g1.add_edge(C, E, 7)
g1.add_edge(A, D, 3)
g1.add_edge(D, G, 5)

g1.show_graph()
