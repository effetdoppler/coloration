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

def __Dsaturverctice(G, result):
    dsatur = []
    maximum = 0
    ind = 0
    for i in range(G.order):
        if result[i] == -1:
            color = []
            dsatur.append([i, 0])
            for adj in G.adjlists[i]:
                if result[adj] not in color and result[adj] != -1:
                    color.append(result[adj])
                    dsatur[ind][1] += 1
            maximum = max(maximum, dsatur[ind][1])
            ind += 1
    ind = len(dsatur) - 1
    while ind >= 0:
        if dsatur[ind][1] != maximum:
            del dsatur[ind]
        ind -= 1
    if len(dsatur) == 1:
        return dsatur[0][0]

    degrees = []
    for vert in dsatur:
        degree = 0
        for adj in G.adjlists[vert[0]]:
            if result[adj] == -1:
                degree += 1
        degrees.append(degree)
    ind = 0
    act = degrees[0]
    for i in range(1, len(degrees)):
        if act < degrees[i]:
            ind = i
            act = degrees[i]
    return dsatur[ind][0]


def color_dsatur(G):
    result = [-1] * G.order
    result[0] = 0
    nbcolor = 1
    color = [0]
    available = [False] * G.order
    trace = [False] * G.order
    trace[0] = True
    while trace != [True] * G.order:
        i = __Dsaturverctice(G, result)
        trace[i] = True
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
