import sys

#顶点类

class Vertex:
    """ Vertex class to store vertex details
    """
    def __init__(self, name , propert):
        self.name = name                   #节点名称        
        self.propert = propert             #节点属性
        self.adj = []                      #邻接点
        self.status = True                 #记录是否遍历 
        self.d = [sys.maxsize] #           #存储最短路径值
        self.pi = None                     #存储最近的源节点


    def setKeyForHeap(self, d):            
        self.d = d
        return True

    def addEdge(self, edge):
        self.adj.append(edge)

    def getEdgeFromVertex(self, dest):
        for temp in self.adj:
            if dest == temp.destination:
                return temp
        return None


