class MinHeap:

    def __init__(self, data, key):
        self.aHeapsize = 0
        self.data = data
        self.key = key
        self.build_heap()

    def parent(self, i):
        return (i-1)//2

    def left(self, i):
        return 2*i + 1

    def right(self, i):
        return 2*i+2

    def min_heapify(self, i):

        l = self.left(i)
        r = self.right(i)
        smallest = i

        if l < self.aHeapsize and self.key(self.data[l]) < self.key(self.data[i]):
            smallest = l

        if r < self.aHeapsize and self.key(self.data[r]) < self.key(self.data[smallest]):
            smallest = r

        if smallest != i:
            if smallest == l:
                if l < self.aHeapsize:
                    self.data[l].position = i
                self.data[i].position = l
                if r < self.aHeapsize:
                    self.data[r].position = r
            elif smallest == r:
                if r < self.aHeapsize:
                    self.data[r].position = i
                self.data[i].position = r
                if l < self.aHeapsize:
                    self.data[l].position = l

            self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
            self.min_heapify(smallest)
        else:
            if l < self.aHeapsize:
                self.data[l].position = l
            self.data[i].position = i
            if r < self.aHeapsize:
                self.data[r].position = r

    #初始化堆
    def build_heap(self):                                                       #O(n)
        self.aHeapsize = len(self.data)
        loc_i = self.parent(self.aHeapsize - 1)
        while loc_i >= 0:
            self.min_heapify(loc_i)
            loc_i -= 1
        return self.data

    #输出当前距离最小节点
    def extractMin(self):                                                       #O(log(n))
        if self.aHeapsize < 1:
            return None

        minimum = self.data[0]
        self.data[0] = self.data[self.aHeapsize-1]
        self.aHeapsize -= 1
        if self.aHeapsize > 0:
            self.min_heapify(0)
        return minimum

    #堆中减少节点时，更新堆信息
    def heapDecreaseKey(self, node, newValue, setKeyFunction):
        
        if newValue > self.key(node):          # new value should be smaller than the old one
            return False

        i = node.position                                                       # index
        setKeyFunction(newValue)
        while i > 0 and self.key(self.data[self.parent(i)]) > self.key(self.data[i]):
            self.data[self.parent(i)].position, self.data[i].position = \
                self.data[i].position, self.data[self.parent(i)].position
            self.data[self.parent(i)], self.data[i] = self.data[i], self.data[self.parent(i)]
            i = self.parent(i)
        return True

    def __len__(self):
        return self.aHeapsize