graph = {
    "SB": 4,
    "SC": 2,
    "BC": 1,
    "BD": 5,
    "CD": 8,
    "CE": 10,
    "DT": 6,
    "DE": 2,
    "ET": 3
}


def loop(g, c, t, s, weight, order, done):
    keys = [x.find(c) for x in g]
    links = {i.replace(c,""):graph[i] for x, i in enumerate(graph) if keys[x] > -1}
    links = {x:links[x] for x in links if not done[x]}

    for x in links:
        if weight[x] > weight[c] + links[x]:
            weight[x] = weight[c] + links[x]
            order[x] = c

    done[c] = True

    sort = sorted(weight.items(), key=lambda item: item[1])
    nc = [k[0] for k in sort if not done[k[0]]][0]

    if nc is not t:
        loop(g, nc, t, s, weight, order, done)
    else:
        print(viz(order, t, s))


def viz(o, n, s):
    if n is not s:
        return viz(o, o[n], s) + " -> " + n
    else:
        return s


def start(g, s = "S", t = "T"): 
    weight = {}
    order = {}
    done = {}

    keys = set(''.join(graph.keys()))
    order = {k:'' for k in keys}
    done = {k:False for k in keys}
    weight = {k:(999999 if k is not s else 0) for k in keys}

    loop(g, s, t, s, weight, order, done)


start(graph)