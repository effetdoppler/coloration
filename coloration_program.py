from algopy import graph

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

# https://www.researchgate.net/publication/311916215_A_Performance_Comparison_of_Graph_Coloring_Algorithms
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
        # find the maximum degree in X
        indm = -1
        maximum = -1
        for i in range(len(x)):
            deg = len(x_adjlists[i])
            if deg < maximum:
                continue
            if deg > maximum or len(G.adjlists[x[i]]) > len(G.adjlists[x[indm]]):
                indm = i
                maximum = deg

        Si.append(x[indm])
        del x[indm]

        u = set()
        vv = set(x)
        for v in x:
            if v in x_adjlists[Si[-1]]:
                u.add(v)
                vv.remove(v)
        while x:
            for v in x_adjlists[Si[-1]]:
                if v not in u:
                    u.add(v)
                    vv.remove(v)
            maximum = -1
            candidates = []
            for v in vv:
                # calculate number of neighbors that are adjacent to vertices in Si
                nbneighbor = 0
                for adj in x_adjlists[v]:
                    if adj in u:
                        nbneighbor += 1
                if nbneighbor < maximum:
                    continue
                elif nbneighbor == maximum:
                    candidates.append(v)
                else:
                    maximum = nbneighbor
                    candidates = [v]

            if len(candidates) == 0:
                break
            v = candidates[0]
            Si.append(v)
            x.remove(v)
            vv.remove(v)

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

def __ido_step3(G, color, M):
    maxcol_ind = []
    maxcol = 0
    # The number of the colored adjacent vertices is calculated for every uncolored vertices.
    for i in range(G.order):
        if not M[i]:
            nbcolor = 0
            for adj in G.adjlists[i]:
                if color[adj] != -1:
                    nbcolor += 1
            if maxcol < nbcolor:
                maxcol = nbcolor
                maxcol_ind = [i]
            elif maxcol == nbcolor:
                maxcol_ind.append(i)
    # the uncolored vertex whose colored neighboring vertices are the maximum is selected.
    if len(maxcol_ind) == 1:
        return maxcol_ind[0]
    # If more than one vertex provides this condition, the vertex which has the largest degree is selected.
    ind = maxcol_ind[0]
    maximum = 0
    for el in maxcol_ind:
        if maximum < len(G.adjlists[el]):
            ind = el
            maximum = len(G.adjlists[el])
    return ind

# https://www.researchgate.net/publication/311916215_A_Performance_Comparison_of_Graph_Coloring_Algorithms
def color_ido(G):
    M = [False] * G.order
    color = [0]
    result = [-1] * G.order
    maximum = 0
    nbcolor = 1
    ind = 0
    for i in range(G.order):
        if len(G.adjlists[i]) > maximum:
            ind = i
            maximum = len(G.adjlists[i])
    # Step 2: The vertex that has the largest degree is colored with the first color
    result[ind] = color[0]
    M[ind] = True
    available = [False] * G.order
    while M != [True] * G.order:
        ind = __ido_step3(G, result, M)
        M[ind] = True
        for y in G.adjlists[ind]:
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
        result[ind] = cr
        for y in G.adjlists[ind]:
            if result[y] != -1:
                available[result[y]] = False

    for i in range(len(result)):
        result[i] += 1
    return nbcolor, result







