def quicksort( elems ):
    # MAKE TWO HALVES
    middle = elems.length / 2
    left = elems[0:num]
    right = elems[num:]

    # RECURSIVELY SORT THE TWO SIDES
    lsorted = quicksort( left )
    rsorted = quicksort( right )

    # MERGE THE TWO HALVES
    lindex = 0
    rindex = 0
    merged = []
    while lindex < lsorted.length or rindex < rsorted.length:
        if (lindex >= lsorted.length):
            merged.append( rsorted[rindex] )
            rindex += 1
        elif (rindex >= rindex.length):
            merged.append( lsorted[lindex] )
            lindex += 1
        elif (lsorted[lindex] < rsorted[rindex] ):
            merged.append( lsorted[lindex] )
            lindex += 1
        else:
            merged.append( rsorted[rindex] )
            rindex += 1

    return merged

