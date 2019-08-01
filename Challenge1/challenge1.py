from graph import Vertex, Graph
import string
import re
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        graph_file = sys.argv[1]
    else:
        graph_file = './graph_data.txt'

    with open(graph_file, 'r') as f:
        graph_data = []
        for line in f:
            x = line.strip('()\n').split(',')
            graph_data.append(x)
    
    i = 0
    edges_list = []
    while i < len(graph_data):
        if i == 1:
            vert_list = graph_data[i]
        elif i > 1:
            edges_list.append(graph_data[i])
        i += 1

    g = Graph()

    for item in vert_list:
        g.add_vertex(item)
    
    for item in edges_list:
        if len(item) == 3:
            g.add_edge(item[0], item[1], item[2])
        elif len(item) == 2:
            g.add_edge(item[0], item[1])
    
    # print(vert_list)
    # print(edges_list)
    
    # # Challenge 1: Create the graph

    # g = Graph()

    # # Add your friends
    # g.add_vertex("Friend 1")
    # g.add_vertex("Friend 2")
    # g.add_vertex("Friend 3")
    # g.add_vertex("Friend 4")
    # g.add_vertex("Friend 5")
    # g.add_vertex("Friend 6")
    # g.add_vertex("Friend 7")
    # g.add_vertex("Friend 8")
    # g.add_vertex("Friend 9")
    # g.add_vertex("Friend 10")

    # # ...  add all 10 including you ...

    # # Add connections (non weighted edges for now)
    # g.add_edge("Friend 1", "Friend 2")
    # g.add_edge("Friend 2", "Friend 3")
    # g.add_edge("Friend 3", "Friend 4")
    # g.add_edge("Friend 4", "Friend 5")
    # g.add_edge("Friend 5", "Friend 6")
    # g.add_edge("Friend 7", "Friend 8")
    # g.add_edge("Friend 8", "Friend 9")
    # g.add_edge("Friend 9", "Friend 10")

    # # Challenge 1: Output the vertices & edges
    # # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")
    
    print('# Vertices: %s' % (len(vert_list)))
    print('# Edges: %s' % (len(edges_list)))

    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            key1 = v.get_id()
            key2 = w.get_id()
            # weight = v.get_edge_weight(w)
            print("( %s , %s , %s)" % (key1, key2, v.get_edge_weight(w)))
