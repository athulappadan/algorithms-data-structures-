# kruskal algorithm

import mst
import min_heap
import QF

def kruskalPaths(G):
        k_mst = mst.MST()
        pq = min_heap.PQ()
        uf = QF.UF(G.V)

        for e in G.allEdges():
                pq.insert(e)

        while (not pq.isEmpty() and k_mst.size() < G.V - 1):
                e = pq.delMin()
                v = e.either()
                w = e.other(v)

                if (not uf.connected(v, w)):
                        uf.union(v, w)
                        k_mst.push_edge(e)


        return k_mst

def show_mst(k_mst):
        for e in k_mst.edges():
                print(e.v, e.w, e.weight)

G = mst.G
kl = kruskalPaths(G)
show_mst(kl)
