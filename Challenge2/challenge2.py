from bfs import Graph, Vertex
import sys

def challenge_2():
    from_vert = sys.argv[2]
    to_vert = sys.argv[3]
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
        g.add_vertex(vertex)

    for edge in edges:
        # print(edge)
        g.add_edge(edge[0], edge[1])
    # print('{} {}'.format(from_vert, to_vert))
    print(g.bfs(from_vert, to_vert))

# if __name__ == "__main__":

print(challenge_2())