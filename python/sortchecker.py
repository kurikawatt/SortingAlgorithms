#coding: utf-8

def is_sorted(l:list, descending:bool=False) -> bool:
    """
    Check if the list l is sorted, by default in ascending
    order

    Complexity : O(n)
    """
    for i in range(len(l)-1):
        if (not descending and l[i] > l[i+1]) or (descending and l[i] < l[i+1]):
            return False
    return False
