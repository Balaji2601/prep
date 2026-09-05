"""
Disjoint set union or Union find consists of two main operations
Operation1: Union - 
Operation2: Find - To find an element belongs to which set/parent.

We have to maintain a parent(to know who is parent of given element) list and elements list.
"""

from typing import List


def find(i: int, parent: List[int]): # function name can also be find_parent(i)
    if parent[i] == i:
        return i
    return find(parent[i], parent)

def union(x, y, parent):
    parent_of_x = find(x, parent)
    parent_of_y = find(y, parent)

    if parent_of_x != parent_of_y:
        parent[parent_of_x] = parent_of_y