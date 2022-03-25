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


# Set Output
def key_output(count, S):
    print(count)
    if len(S) != 0:
        for idx in range(len(S)):
            print(len(S[idx][1]), S[idx][0], sep=' ')
            print(*S[idx][1], sep=' ')


# Class for MST by Kruskal's Algorithm
class Graph:
    def __init__(self, v, e, edges):
        self.edge = e
        self.vertex = v
        self.graph = edges

    def set_init(self, parent, rank, node):
        parent.append(node)
        rank.append(0)

    def query_root(self, parent, node):
        if parent[node - 1] != node:
            parent[node - 1] = self.query_root(parent, parent[node - 1])
        return parent[node - 1]

    def set_union(self, parent, rank, u, v):
        u_root, v_root = self.query_root(parent, u), self.query_root(parent, v)
        if rank[u_root - 1] > rank[v_root - 1]:
            parent[v_root - 1] = u_root
        elif rank[v_root - 1] < rank[u_root - 1]:
            parent[u_root - 1] = v_root
        else:
            parent[v_root - 1] = u_root
            rank[u_root - 1] += 1

    def kruskal(self):
        i = 0
        _tree = []
        _parent = []
        _rank = []

        for node in range(1, self.vertex + 1):
            self.set_init(_parent, _rank, node)

        self.graph = sorted(self.graph, key=lambda edge: edge[2])
        while i < self.edge:
            u, v, w = self.graph[i]
            if self.query_root(_parent, u) != self.query_root(_parent, v):
                _tree.append([u, v, w])
                self.set_union(_parent, _rank, u, v)
            i += 1

        return _tree


# Class for Finding Dual Program Vertex Sets
class Dual:
    def node_init(self, component, parent, node, tree):
        parent.append(node)
        component.append(tree[node][:2])

    def find_parent(self, component, parent, tree):
        for i in range(len(tree)):
            for j in range(0, i):
                if bool(set(component[j]) & set(component[i])) is True:
                    component[i] = list(set().union(component[i], component[j]))
                    if parent[j] == j:
                        parent[j] = i

    def soldual(self, tree):
        count = 0
        S = []
        _component = []
        _parent = []

        for edge in range(len(tree)):
            self.node_init(_component, _parent, edge, tree)

        self.find_parent(_component, _parent, tree)
        for i in range(len(tree) - 1):
            if tree[_parent[i]][2] - tree[i][2] != 0:
                count += 1
                S.append([tree[_parent[i]][2] - tree[i][2], _component[i]])

        if tree[-1][2] != 0:
            S.append([tree[-1][2], _component[-1]])
            count += 1

        return count, S


if __name__ == "__main__":
    n, m, edge_list = key_input()
    g = Graph(n, m, edge_list)
    count, S = Dual().soldual(g.kruskal())
    key_output(count, S)
