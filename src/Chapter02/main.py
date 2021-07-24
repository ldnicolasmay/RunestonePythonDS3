from ms_die import MSDie

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)


x = MSDie(6)
y = MSDie(5)
 
print(x)
print(y)
print(x == y)
print(x < y)
print(x > y)
print(x != y)
print(x <= y)
print(x >= y)
print(x is y)

