class HashTable:

    def __init__( self, hashfunc, size = 16, max_load = .75 ):
        self.hashfunc = hashfunc
        self.size = size
        self.elems = [[] for i in range(size)]
        self.max_load = max_load
        self.count = 0

    def insert( self, key, object ):
        self.count += 1
        index = self.hashfunc( key ) % self.size
        self.elems[index].append( HashObject(key, object) )

    def remove( self, key ):
        index = self.hashfunc( key ) % self.size
        for elem in self.elems[index]:
            if (elem.key == key):
                self.elems[index].remove(elem)
                self.count -= 1
                return

    def get( self, key ):
        index = self.hashfunc( key ) % self.size
        for elem in self.elems[index]:
            if (elem.key == key):
                return elem.object
        return None

    def get_elems( self ):
        elems = []
        for i in range(self.size):
            elems += self.elems[i]
        return elems

    def resize ( self ):
        new_size = self.size * 2
        bigger = HashTable( self.hashfunc, new_size, self.max_load )
        for elem in self.get_elems():
            bigger.insert(elem.key, elem.object)
        return bigger


class HashObject:
    def __init__( self, key, object ):
        self.key = key
        self.object = object
