
def is_balanced( node ):

    if node is None:
        return 0, True

    left_height, left_balanced = is_balanced( node.left )
    right_height, right_balanced = is_balanced( node.right )

    my_height = max([left_height, right_height]) + 1
    print(left_height, right_height, my_height)

    if not left_balanced or not right_balanced:
        return my_height, False

    if abs(left_height - right_height) > 1:
        return my_height, False

    return my_height, True

class Node:
    def __init__( self, val, left, right ):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    lines = [
        '-2 -1 -1',
        '0 -2 -1',
        '1 0 -1',
        '2 -1 -1',
        '3 -1 -1',
        '4 -1 -1',
        '5 1 2',
        '6 3 4',
        '7 5 6' ]
    print(lines)
    nodes = {}
    root = None
    for line in lines:
        nums = [int(x) for x in line.split(' ')]
        val = nums[0]
        left = None if nums[1] is -1 else nodes[nums[1]]
        right = None if nums[2] is -1 else nodes[nums[2]]
        n = Node( val, left, right )
        nodes[val] = n
        root = n
    print(root)
    print(is_balanced( root ))
