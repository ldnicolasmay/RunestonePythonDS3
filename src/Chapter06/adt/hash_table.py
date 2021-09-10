class HashTable(object):

    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def _rehash_function(self, old_key):
        return (old_key + 1) % self.size

    def put(self, key, value):
        position = self._hash_function(key)

        if self.values[position] is None:
            self.keys[position] = key
            self.values[position] = value
        else:
            if self.keys[position] == key:
                self.values[position] = value  # replace
            else:
                position = self._rehash_function(position)
                while (
                    self.keys[position] is not None and
                    self.keys[position] != key
                ):
                    position = self._rehash_function(position)

                if self.keys[position] is None:
                    self.keys[position] = key
                    self.values[position] = value
                else:
                    self.values[position] = value

    def get(self, key):
        start_position = self._hash_function(key)
        position = start_position

        while self.keys[position] is not None:
            if self.keys[position] == key:
                return self.values[position]
            else:
                position = self._rehash_function(position)
                if position == start_position:
                    return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)
