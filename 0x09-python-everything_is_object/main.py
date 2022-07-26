def increment(n):
    n += 1
    return n
a = 1
A = increment(a)
print(A)
def incr(n):
    n.append(4)
l = [1, 2, 3]
incr(l)
print(l)
def assign_value(n, v):
        n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
a = ()
print(type(a))
a = (1, 2)
b = (1, 2)
print(a is b)
a = ()
b = ()
print(a is b)
