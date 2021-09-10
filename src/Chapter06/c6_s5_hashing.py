# from typing import

from adt.hash_table import HashTable


def hash_str(s: str, table_size: int) -> int:
    return sum([ord(ch) for ch in s]) % table_size


print(hash_str("cat", 11))


def weighted_hash_str(s: str, table_size: int) -> int:
    return sum([(pos + 1) * ord(ch) for pos, ch in enumerate(s)]) % table_size


print(weighted_hash_str("cat", 11))


h = HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
h[17] = "tiger"
h[77] = "bird"
h[31] = "cow"
h[44] = "goat"
h[55] = "pig"
h[20] = "chicken"
print(h.keys)
print(h.values)
h[20] = "duck"
print(h.keys)
print(h.values)
print(h[20])
print(h[99])
