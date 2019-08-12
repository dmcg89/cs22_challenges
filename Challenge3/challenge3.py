from graph import Graph, Vertex
import sys

def challenge_3():
    from_vert = int(sys.argv[2])
    to_vert = int(sys.argv[3])
    # print(from_vert)
    # print(to_vert)
    vertex_list = []
    edges = []
    counter = 0
    with open(sys.argv[1], 'r') as f:
        #graph_data = f.readlines()
        for line in f:
            x = line.strip('()\n').split(',')
            # counter at 1 indicates the input list or the vert list
            if counter == 1:
                vertex_list = x
            counter += 1
            # counter > 2 indicates the edges
            if counter > 2:
                edges.append(x)
           
    g = Graph()
    for vertex in vertex_list:
        vertex = int(vertex)
        g.add_vertex(vertex)

    for edge in edges:
        # print(edge)
        g.add_edge(int(edge[0]), int(edge[1]))
    # print(edges)
    # print(vertex_list)

    return(g.find_path(from_vert, to_vert))

# if __name__ == "__main__":

print(challenge_3())