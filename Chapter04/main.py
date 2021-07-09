from stack import Stack

s = Stack()

print(f"{s}")
print(f"{s.is_empty()}", end="\n\n")

s.push(4)
print(f"{s}", end="\n\n")

s.push('dog')
print(f"{s}", end="\n\n")

print(s.peek())
print(f"{s}", end="\n\n")

s.push(True)
print(f"{s}", end="\n\n")

print(s.size())
print(f"{s}", end="\n\n")

print(s.is_empty())
print(f"{s}", end="\n\n")

s.push(8.4)
print(f"{s}", end="\n\n")

print(s.pop())
print(f"{s}", end="\n\n")

print(s.pop())
print(f"{s}", end="\n\n")

print(s.size())
print(f"{s}", end="\n\n")

