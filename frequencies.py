"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        x = str(i)
        if not x in frequencies:
            frequencies[x] = 1
        else:
            frequencies[x] += 1
    return frequencies

