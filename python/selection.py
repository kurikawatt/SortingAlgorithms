#coding: utf-8

def selection_sort(l:list) -> None:
    """
    Selection sort
    """
    size_l = len(l)
    for i in range(size_l):
        mini = i
        for j in range(i, size_l):
            if l[j] < l[mini]:
                mini = j
        if i != mini:
            l[i], l[mini] = l[mini], l[i]

