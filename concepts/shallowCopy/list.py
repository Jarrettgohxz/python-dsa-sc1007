l = [1, 2, 3, [4, 5, 6], {'hello': 'test'}]
# l2 = l.copy()
l2 = l[0:len(l)]  # works to create a shallow copy too


def example1():
    # doesn't modify the original variable 'd'
    # 2nd element is an integer (immutable)
    l2[2] = 4


def example2():
    # doesn't modify the original variable 'd'
    # simply make l2 point to a new list
    l2[3] = [6, 7, 8]


def example3():
    l2[3][1] = 6


def example4():
    # doesn't modify the original variable 'd'
    # simply make l2 point to a new dict
    l2[4] = {'test': 'hello'}


def example5():
    # mutates the original 'd' variable too
    # dict is a mutable object
    l2[4]['hello'] = 'HELLO FRIEND'


example1()
# example2()
example3()
# example4()
# example5()

print(l)
print(l2)
