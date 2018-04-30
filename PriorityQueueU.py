#
#	Definicao da classe pilha de prioridade
#

import heapq

class PriorityQueue:
    def __init__(self):
        self.lstElements = []

    def empty(self):
        return (len(self.lstElements) == 0)

    def put(self, item, priority):
        heapq.heappush(self.lstElements, (priority, item))

    def get(self):
        return heapq.heappop(self.lstElements)[1]
