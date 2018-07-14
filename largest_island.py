import numpy as np

def largest_island( tiles ):
    assert(len(tiles.shape) == 2)

    land = make_land( tiles )

    # GET THE ISLAND SIZE AT EACH TILE
    # SKIP TILES THAT HAVE ALREADY BEEN INCORPORATED IN AN ISLAND
    max_size = 0
    for x in range( land.shape[0] ):
        for y in range( land.shape[1] ):
            size = size_at( land, x, y )
            set_not_visited( land )
            if (size > max_size):
                max_size = size
    return max_size

def make_land( tiles ):
    land = np.empty( tiles.shape, dtype=object )
    for x in range( tiles.shape[0] ):
        for y in range( tiles.shape[1] ):
            land[x][y] = Tile( tiles[x][y] == 1 )
    return land

def size_at( tiles, x, y ):
    # NOT LAND
    if (tiles[x][y].is_land == False):
        return 0

    # ALREADY COUNTED
    if (tiles[x][y].visited):
        return 0

    # ALREADY DISCOVERED ISLAND
    if (tiles[x][y].used):
        return 0

    print(x, y)
    tiles[x][y].visited = True
    tiles[x][y].used = True
    size = 1
    if (x > 0):
        size += size_at(tiles, x - 1, y)
    if (x < tiles.shape[0] - 1):
        size += size_at(tiles, x + 1, y)
    if (y > 0):
        size += size_at(tiles, x, y - 1)
    if (y < tiles.shape[1] - 1):
        size += size_at(tiles, x, y + 1)

    return size

def set_not_visited( tiles ):
    for x in range( tiles.shape[0] ):
        for y in range( tiles.shape[1] ):
            tiles[x][y].visited = False

class Tile:
    def __init__( self, is_land ):
        self.is_land = is_land
        self.visited = False
        self.used = False

if __name__ == "__main__":
    tiles = np.zeros((5, 5))
    tiles[0,0:2] = 1
    tiles[:,3] = 1
    tiles[2, 2:5] = 1
    tiles[3,0:2] = 1
    tiles[4,0:2] = 1
    tiles[1,4] = 1
    tiles[3,2] = 1

    land = make_land( tiles )
    print(tiles)
    print(size_at(land, 0, 0))
    print(size_at(land, 0, 3))
    print(largest_island( tiles ))