from itertools import combinations, permutations
import matplotlib.pyplot as plt
import networkx as nx


def build_maze(filename):
    with open(filename) as f:
        lines = f.read().split()
    maze = nx.Graph()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char != "#":
                node = row, col
                maze.add_node(node, label=char)
                for neighbor in [(row - 1, col), (row, col - 1)]:
                    if neighbor in maze:
                        maze.add_edge(node, neighbor, weight=1)
                if char == "@":
                    start = node
    orig = maze.copy()
    for n in list(maze):
        if maze.nodes[n]["label"] == ".":
            for (
                p,
                q,
            ) in combinations(maze[n], 2):
                weight = maze.edges[p, n]["weight"] + maze.edges[n, q]["weight"]
                maze.add_edge(
                    p,
                    q,
                    weight=weight
                    if (p, q) not in maze.edges
                    else min(weight, maze.edges[p, q]["weight"]),
                )
            maze.remove_node(n)
    for (
        p,
        q,
        w,
    ) in maze.edges.data("weight"):
        assert w == nx.shortest_path_length(orig, p, q, "weight")
    return maze, start


def calculate_dependencies(maze, start):
    deps = nx.DiGraph()
    for p, q in permutations(maze.nodes, 2):
        p_label, q_label = maze.nodes[p]["label"], maze.nodes[q]["label"]
        if q_label.islower() and p_label != "@":
            deps.add_node(q_label, label=q_label)
            copy = maze.copy()
            copy.remove_node(p)
            if not nx.has_path(copy, start, q):
                dep = p_label.lower()
                deps.add_node(dep, label=dep)
                deps.add_edge(dep, q_label)
    return deps


def draw_graph(graph, edges=True):
    plt.clf()
    pos = nx.drawing.nx_agraph.graphviz_layout(graph, prog="neato")
    nx.draw(graph, pos, labels=dict(graph.nodes.data("label")))
    if edges:
        nx.draw_networkx_edge_labels(
            graph, pos, {(p, q): w for p, q, w in graph.edges.data("weight")}
        )
    plt.show()


def score_route(maze, start, route):
    return len(maze) + len(start) + len(route)  # todo


def main():
    maze, start = build_maze("example2.txt")
    # draw_graph(maze)
    deps = calculate_dependencies(maze, start)
    # draw_graph(deps, False)
    print(
        min(
            map(
                lambda route: score_route(maze, start, route),
                list(nx.all_topological_sorts(deps)),
            )
        )
    )


if __name__ == "__main__":
    main()
