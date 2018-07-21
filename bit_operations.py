def print_bits( num ):
    bits = ''
    i = 0
    while i < 16: 
        bit = (num & 1)
        bits = str(bit) + bits
        num = num >> 1
        i += 1
        if i % 4 == 0 and i != 16:
            bits = ' ' + bits

    print( bits )

def insert_bits( n, m, i, j ):
    print_bits( n )
    print_bits( m )

    mask = -1
    mask = mask << (j - i + 1)
    for x in range(i):
        mask = (mask << 1) + 1

    val = (n & mask) | (m << i)
    print_bits( val )
    return val

if __name__ == '__main__':
    insert_bits( 64, 6, 3, 5 )