#coding: utf-8

def insertion_sort(l:list) -> list:
    """
    Insertion sort
    """
    for i in range(1, len(l)):
        v = l[i]
        j = i
        while j > 0 and l[j-1] > v:
            l[j] = l[j-1]
            j -= 1
        l[j] = v
