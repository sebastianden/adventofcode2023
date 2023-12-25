# Answer: 601344

import graphviz


def count_nodes(start, graph):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            if node in graph:
                queue.extend(graph[node])
            for i in graph:
                if node in graph[i]:
                    queue.append(i)
            visited.add(node)

    return len(visited)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()

    graph = {}
    for line in data:
        k, v = line.split(':')
        v = v.split(' ')
        graph[k] = [x for x in v if x != '']

    # cth -> xxk
    # zdj -> nvt
    # mzg -> bbm
    graph['cth'] = [n for n in graph['cth'] if n != 'xxk']
    graph['zdj'] = [n for n in graph['zdj'] if n != 'nvt']
    graph['mzg'] = [n for n in graph['mzg'] if n != 'bbm']

    n = graphviz.Digraph(engine='neato', format='svg')

    for k, v in graph.items():
        for i in v:
            n.node(k)
            n.edge(k, i)
    # n.render('graph.gv', view=True)

    print(count_nodes('cth', graph)*count_nodes('xxk', graph))
