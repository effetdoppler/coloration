from algopy.graph import Graph

"""
GREEDY COLORATION
"""
def color_greedy(G):
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


def color_weslsh_powell(G):
    nbcolor = 0
    if G.order == 0:
        return nbcolor, []
    result = [-1] * G.order

    # sort degree in ascending order
    degree = []
    i = 0
    for i in range(G.order):
        degree.append((i, len(G.adjlists[i])))
    degree.sort(key=lambda x: x[1])
    # keep only the vertices
    degree = [v[0] for v in degree]

    while degree:
        nbcolor += 1
        # work from back to front
        result[degree[len(degree)-1]] = nbcolor
        # remove the last one
        del degree[len(degree)-1]
        for i in range(len(degree)-1, -1, -1):
            v = degree[i]
            # if no neighbor is colored
            good = True
            for adj in G.adjlists[v]:
                if result[adj] == nbcolor:
                    good = False
                    break
            if good:
                # color the vertex
                result[v] = nbcolor
                # remove it from the degree list
                del degree[i]

    return nbcolor, result


def color_rlf(G):
    nbcolor = 0
    if G.order == 0:
        return nbcolor, []
    result = [-1] * G.order

    x_adjlists = G.adjlists.copy()
    x = list(range(G.order))

    while x:
        nbcolor += 1
        # Si will be colored by nbcolor
        Si = []
        # find the max degree in X
        indM = -1
        max = -1
        for i in range(len(x)):
            deg = len(x_adjlists[i])
            if (deg < max):
                continue
            if (deg > max or len(G.adjlists[x[i]]) > len(G.adjlists[x[indM]])):
                indM = i
                max = deg

        Si.append(x[indM])
        del x[indM]

        while x:
            candidates = []
            max = -1
            for i in range(len(x)):
                # not currently adjacent to any vertex in Si
                good = True
                for adj in x_adjlists[x[i]]:
                    if adj in Si:
                        good = False
                        break
                if not good:
                    continue
                # calculate number of neighbors that are adjacent to vertices in Si
                nbneighbor = 0
                for adj in x_adjlists[x[i]]:
                    for adjj in x_adjlists[adj]:
                        if adjj in Si:
                            nbneighbor += 1
                            break
                if nbneighbor < max:
                    continue
                elif nbneighbor == max:
                    candidates.append(i)
                else:
                    max = nbneighbor
                    candidates = [i]

            if len(candidates) == 0:
                break
            elif len(candidates) == 1:
                indM = candidates[0]
            else:
                # find the selecting the vertex with the minimum number of neighbors not in Si
                min = G.order
                for i in range(len(candidates)):
                    nbneighbor = 0
                    for adj in x_adjlists[candidates[i]]:
                        if adjj not in Si:
                            nbneighbor += 1
                    if min > nbneighbor:
                        min = nbneighbor
                        indM = candidates[i]
            Si.append(x[indM])
            del x[indM]

        # set nbcolor to Si
        # and remove Si from x_adjlists
        for v in Si:
            result[v] = nbcolor
            x_adjlists[v] = []
        for l in x_adjlists:
            for i in range(len(l)-1, -1, -1):
                if l[i] in Si:
                    del l[i]

    return nbcolor, result




