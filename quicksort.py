def quicksort( elems ):

    # RECURSIVE BASE CASE
    if len(elems) <= 1:
        return elems

    # GET THE QUICKSORT PIVOT ELEMENT
    from statistics import median
    pivot = median([elems[0], elems[-1], elems[len(elems)//2]])

    smaller = [x for x in elems if x < pivot]
    greater = [x for x in elems if x > pivot]
    middle = [x for x in elems if x == pivot]

    smaller = quicksort(smaller)
    greater = quicksort(greater)

    return smaller + middle + greater
