# -*- coding: utf-8 -*-
"""
S4 - Coloration function tests for students
@author: Nathalie
"""

from algopy import graph
import os

def __graphlist(dirpath):
    """builds a list of graphs from a given directory
    Args: 
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        Graph list
    """
    
    files = os.listdir(dirpath)
    files.sort()
    L = []
    for f in files:
        if ".gra" in f:
            L.append(graph.load(dirpath + "/" + f))
    return L
    
# for suscribers of "list comprehensions"

def __graphlist2(dirpath):
    files = os.listdir(dirpath)
    files.sort()
    return [graph.load(dirpath + "/" + f) for f in files if ".gra" in f]
    

#without verification!
def run_coloration(f, dirpath):
    """test coloration function on a list of graphs (without verification)
    Args: 
        f (function): the coloration function (returns (nbcol, color list)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result: list of color numbers
    """
    return [f(G)[0] for G in __graphlist(dirpath)]

# with color verification

def __testcolors(G, colors):
    for s in range(G.order):
        if not colors[s]:
            return False
        for adj in G.adjlists[s]:
            if colors[s] == colors[adj]:
                return False
    return True

def run_verif_coloration(f, dirpath):
    """test the coloration function f on a list of graphs:
        - verify each coloration is correct
        - build the list of resulted chromatic numbers
    Args: 
        f (function): the coloration function (returns (nbcol, color vector)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result list: list of color numbers for each graph
    """
    tests = __graphlist(dirpath)
    results = []
    for G in tests:
        (nb, colors) = f(G)
        if not __testcolors(G, colors):
            results.append((None, "wrong coloration"))
        elif nb != max(colors):
            results.append((nb, "wrong chromatic number"))
        else:
            results.append(nb)
    return results


