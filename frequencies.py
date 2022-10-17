"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    itemstr = map(str, items)
    singleitems = set(map(str,itemstr))
    
    frequencies = {}
    for i in singleitems:
        
        frequencies[i] = itemstr.count(i)    
    
    # Your code goes here
    print(frequencies)
    return frequencies

