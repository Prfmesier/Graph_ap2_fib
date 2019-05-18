from jutge import read

def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]
    for neighbor in graph[vertex]:
        if neighbor not in path:
        	path = dfs_recursive(graph, neighbor, path)

    return path

def main():
	n = read(int)
	m = read(int)
	g = {}
	for x in range(n):
		g[x] = []
	nodes = list()
	for a in range(m):
		primer = read(int)
		segon = read(int)
		l = g[primer]
		l.append(segon)
		g[primer] = l

	x = read(int)
	y = read(int)
	a = dfs_recursive(g,x)
	if(y in a):
		print('yes')
	else:
		print('no')

main()