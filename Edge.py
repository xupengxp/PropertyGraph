
#定义边信息类
class Edges:

    def __init__(self, source, destination, weight,relation):
        self.status = True                #标志位
        self.source = source              #边起点
        self.destination = destination    #边终点
        self.weight = weight              #边权重
        self.relation = relation          #边关系


    def __repr__(self):
        return "Edge data \nstatus : %s source : %s destination : %s weight : %s"\
               % (self.status, self.source, self.destination, self.weight)