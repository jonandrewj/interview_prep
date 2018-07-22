from bit_operations import *

def get_bit( num, index ):
    return (num >> index) & 1

def set_bit( num, index, value ):
    if value == 1:
        num = num | (1 << index)
    else:
        num = num & ~(1 << index)
    return num

def get_first_one( num ):
    index = 0
    while index < 31:
        if get_bit(num, index) == 1 and get_bit(num, index + 1) == 0:
            return index
        index += 1
    return None

def count_ones( num, index ):
    count = 0
    for x in range(index):
        if get_bit(num, x) == 1:
            count += 1
    return count

def next_largest( num ):

    # GET THE PIVOT ONE INDEX
    one_index = get_first_one( num )
    if one_index == None:
        return None

    # GET THE NUMBER OF ONES TO SHIFT TO THE RIGHT
    one_count = count_ones( num, one_index )

    # SWAP THE HIGHER ONE BIT
    num = set_bit(num, one_index + 1, 1)
    num = set_bit(num, one_index, 0)

    # CLEAR THE BITS BEFORE THE PIVOT ONE INDEX
    num = num & ~((1 << one_index) - 1)

    # SET THE FIRST ONE_COUNT BITS TO 1
    for i in range(one_count):
        num = set_bit(num, i, 1)

    return num

def get_pivot( num ):
    for index in range(1, 32):
        if get_bit(num, index) == 1 and get_bit(num, index - 1) == 0:
            return index
    return None

def next_smallest( num ):
    # GET PIVOT ONE
    pivot = get_pivot( num )
    if pivot == None:
        return None

    # GET THE NUMBER OF ONES TO SHIFT TO THE LEFT
    one_count = count_ones( num, pivot )

    # SWAP THE PIVOT INDEX
    num = set_bit(num, pivot, 0)
    num = set_bit(num, pivot - 1, 1)

    # CLEAR THE BITS BEFORE 
    num = num & ~((1 << (pivot - 1)) - 1)

    for i in range( (pivot - one_count) - 1, pivot - 1 ):
        num = set_bit(num, i, 1)

    return num
    

if __name__ == '__main__':
    num = 35
    print_bits( num )
    next = next_largest( num )
    print_bits( next )
    prev = next_smallest( num )
    print_bits( prev )
