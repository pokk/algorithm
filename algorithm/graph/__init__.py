""" Created by wu.jieyi on 2016/03/23. """
import sys

# This is matrix direction graph.
arr_map = [[0, 4, 2, sys.maxsize, sys.maxsize, sys.maxsize],
           [1, 0, sys.maxsize, 2, sys.maxsize, sys.maxsize],
           [sys.maxsize, 3, 0, sys.maxsize, 5, sys.maxsize],
           [sys.maxsize, sys.maxsize, 4, 0, sys.maxsize, 2],
           [sys.maxsize, sys.maxsize, sys.maxsize, 1, 0, sys.maxsize],
           [sys.maxsize, 4, 5, sys.maxsize, 3, 0]]


def draw_graph(arr_graph):
    """
    Draw a directed graph.
    """

    try:
        import matplotlib.pyplot as plt
    except:
        raise
    import networkx as nx

    g = nx.DiGraph()
    edge_set = {}

    # Set the edges and nodes
    for i in range(len(arr_graph)):
        for j in range(len(arr_graph[i])):
            if arr_graph[i][j] is not 0 and arr_graph[i][j] is not sys.maxsize:
                g.add_edge(i, j, weight=0.1)
                edge_set[(i, j)] = arr_graph[i][j]

    # Positions for all nodes.
    pos = nx.spring_layout(g)
    # Nodes
    nx.draw_networkx_nodes(g, pos, node_size=700, node_color="white")
    # Edges
    nx.draw_networkx_edges(g, pos, width=2, alpha=0.5, edge_color='black')
    # Labels
    nx.draw_networkx_labels(g, pos, font_size=15, font_family='sans-serif')
    # Edges' labels
    nx.draw_networkx_edge_labels(g, pos, edge_set, label_pos=0.3)

    plt.axis('off')
    plt.savefig("weighted_graph.png")  # Save as png.
    plt.show()  # Display


def main():
    for i in range(len(arr_map)):
        for j in range(len(arr_map[i])):
            print(arr_map[i][j] if arr_map[i][j] is not sys.maxsize else '∞', end=' ')
        print()

    draw_graph(arr_map)


if __name__ == '__main__':
    main()
