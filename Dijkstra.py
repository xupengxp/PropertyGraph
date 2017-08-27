from MinHeap import *
import sys

#Dijkstra，完成最短路径计算

class Dijkstra:
    def __init__(self):
        self.heap = None                                               # 最小堆
        self.graph = None                                              # 图信息
        self.destination = None                                        # 目标定点
        self.source = None                                             # 源点
        pass

    def dijkstra(self):

        self.initializeSingleSource()
        S = []                                                          #存储已求得最小值的顶点信息
        Q = list(self.graph.vertexMap.values())                         #存储所有顶点
        self.heap = MinHeap(Q, key=lambda vertex: vertex.d)             #最小堆初始化


        while len(self.heap) > 0:
            minDVertex = self.heap.extractMin()
            if not minDVertex.status :
                continue                                                # 通过顶点状态过滤
            S.append(minDVertex)
            for edge in minDVertex.adj:                                 # 检索邻接点，结合最小堆进行松弛过程
                # print("adjacent item is ", edge.destination.name)
                if not edge.status or not edge.destination.status:
                    continue                                            # 跳过已经找到最短路径的点
                nextVertex = edge.destination                           # 通过边获取终点
                weight = edge.weight
                self.Relax(minDVertex, nextVertex, weight)              # 松弛过程     


    #为已经计算的最短路径进行松弛，更新最短路径
    def Relax(self, minDVertex, nextVertex, weight):
        newValue = minDVertex.d + weight
        if nextVertex.d > newValue:
            # nextVertex.d = minDVertex.d + weight
            self.heap.heapDecreaseKey(nextVertex, newValue, nextVertex.setKeyForHeap)
            nextVertex.pi = minDVertex

    #初始化
    def initializeSingleSource(self):                       
        for vertex in self.graph.vertexMap.values():
            vertex.d = sys.maxsize
            vertex.pi = None
        self.source.d = 0


    def minPath(self, graph, source, destination,return_list=True):
        self.graph = graph
        self.destination = graph.vertexMap[destination]
        self.source = graph.vertexMap[source]              

        if return_list:
            path = []

            #遍历节点pi信息，获取最短路径数组
            def traverse(source_inner, destination_inner):
                if destination_inner == source_inner:
                    path.append(destination_inner.name)
                elif destination_inner.pi is None:
                    return
                else:
                    #递归
                    traverse(source_inner, destination_inner.pi)
                    path.append(destination_inner.name)

            self.dijkstra()
            traverse(self.source, self.destination)
            return path,self.destination.d
        else:
            return self.dijkstra()