"""
GREEDY COLORATION
"""
def greedy(G):
    result = [-1] * G.order
    result[0] = 0
    nbcolor = 1
    color = [0]
    available = [False] * G.order
    for i in range(1, G.order):
        for y in G.adjlists[i]:
            if result[y] != -1:
                available[result[y]] = True

        cr = 0
        while cr < G.order:
            if not available[cr]:
                break
            cr += 1

        if cr not in color:
            color.append(cr)
            nbcolor += 1
        result[i] = cr
        for y in G.adjlists[i]:
            if result[y] != -1:
                available[result[y]] = False
    for i in range(len(result)):
        result[i] += 1
    return nbcolor, result

