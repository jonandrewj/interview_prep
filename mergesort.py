def mergesort( elems ):
    # RECURSIVE BASE CASE
    if len(elems) < 2:
        return elems

    # MAKE TWO HALVES
    middle = len(elems) // 2
    left = elems[0:middle]
    right = elems[middle:]

    # RECURSIVELY SORT THE TWO SIDES
    lsorted = mergesort( left )
    rsorted = mergesort( right )

    # MERGE THE TWO HALVES
    lindex = 0
    rindex = 0
    merged = []
    while lindex < len(lsorted) or rindex < len(rsorted):
        if (lindex >= len(lsorted)):
            merged.append( rsorted[rindex] )
            rindex += 1
        elif (rindex >= len(rsorted)):
            merged.append( lsorted[lindex] )
            lindex += 1
        elif (lsorted[lindex] < rsorted[rindex] ):
            merged.append( lsorted[lindex] )
            lindex += 1
        else:
            merged.append( rsorted[rindex] )
            rindex += 1

    return merged

