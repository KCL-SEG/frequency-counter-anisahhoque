"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    itemstr = map(str, items)
    singleitems = set(map(str,itemstr))
    
    frequencies = {}
    for i in singleitems:
        
        frequencies[i] = list(itemstr).count(i)    
    

    return frequencies

