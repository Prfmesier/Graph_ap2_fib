from jutge import read


def bfs(graph, root):
    visited, queue = set(), [root]
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited and not in queue:
                visited.add(neighbour)
                queue.append(neighbour)
    return visited


n = read(int)
nodes = read(str, amount=n)


g = {}
for node in nodes:
    g[node] = []

m = read(int)
for i in range(m):
    edge = read(str, str)
    g[edge[0]].append(edge[1])

cami = read(str, str)


conex = bfs(g, cami[0])

if cami[1] in conex:
    print('yes')
else:
    print('no')
