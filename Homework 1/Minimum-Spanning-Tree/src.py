# Read Input
def key_input():
    edge_list = []
    n, m = map(int, input().split())

    for edge_idx in range(m):
        try:
            edge_list.append(list(map(int, input().split())))
        except:
            break

    return n, m, edge_list


# Class for MST by Kruskal's Algorithm
class Graph:
    def __init__(self, v, e, edges):
        self.vertex = v
        self.edge = e
        self.graph = edges

        self._parent = []
        self._rank = []
        self._tree = []

        for node in range(1, self.vertex+1):
            self.set_init(node)

    def set_init(self, node):
        self._parent.append(node)
        self._rank.append(0)

    def query_root(self, node):
        if self._parent[node-1] != node:
            self._parent[node-1] = self.query_root(self._parent[node-1])
        return self._parent[node-1]

    def set_union(self, u, v):
        u_root, v_root = self.query_root(u), self.query_root(v)
        if self._rank[u_root-1] > self._rank[v_root-1]:
            self._parent[v_root-1] = u_root
        elif self._rank[v_root-1] < self._rank[u_root-1]:
            self._parent[u_root-1] = v_root
        else:
            self._parent[v_root-1] = u_root
            self._rank[u_root-1] += 1

    def kruskal(self):
        i, j = 0, 0
        self.graph = sorted(self.graph, key=lambda edge: edge[2])
        print(self._parent)

        while i < self.edge:
            u, v, w = self.graph[i]
            print(u, v)

            if self.query_root(u) != self.query_root(v):
                self._tree.append([u, v, w])
                self.set_union(u, v)
                # print("Selected edge: {a}-{b}: {c}".format(a=u, b=v, c=w))

            i += 1

        # print("MST as edge form [u, v, weight] as follows: \n")
        # print(self._tree)
        return self._tree


if __name__ == "__main__":
    n, m, edge_list = key_input()
    g = Graph(n, m, edge_list)
    MST = g.kruskal()


