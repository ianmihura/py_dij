import json


class Graph:
    def __init__(self, graph: dict, start_node = "S", end_node = "T"):
        """Params:
        graph of the shape: {'AB': 2, ...}
            A & B being nodes conected with an edge of weight 2
        start_node & end_node single char string"""

        self.g = graph
        self.s = start_node
        self.t = end_node

        self.weight = {}
        self.order = {}
        self.done = {}

        keys = set(''.join(self.g.keys()))
        self.order = {k:'' for k in keys}
        self.done = {k:False for k in keys}
        self.weight = {k:(999999 if k is not self.s else 0) for k in keys}


    def __call__(self):
        self._loop(self.s)


    def _loop(self, c: str):
        """Internal funcion. 
        Takes a current node for evaluation c (single char string)"""
        keys = [x.find(c) for x in self.g]
        links = {i.replace(c,""):self.g[i] for x, i in enumerate(self.g) if keys[x] > -1}
        links = {x:links[x] for x in links if not self.done[x]}

        for x in links:
            if self.weight[x] > self.weight[c] + links[x]:
                self.weight[x] = self.weight[c] + links[x]
                self.order[x] = c

        self.done[c] = True

        sort = sorted(self.weight.items(), key=lambda item: item[1])
        nc = [k[0] for k in sort if not self.done[k[0]]][0]

        if nc is not self.t:
            self._loop(nc)


    def __str__(self):
        return self._viz(self.t)


    def __repr__(self):
        return f'Graph(graph={self.g}, path="{self._viz(self.t)}", path_weight={self.weight[self.t]})'


    def _viz(self, n: str):
        """Internal function.
        Takes a node n that is the last node of the path (single char string)"""
        if n is not self.s:
            return self._viz(self.order[n]) + " -> " + n
        else:
            return self.s


if __name__ == "__main__":
    with open('graph.json') as f:
        json_graph = json.load(f)

    graph = Graph(json_graph)
    graph()
    print(graph.__repr__())
    print(graph.__str__())