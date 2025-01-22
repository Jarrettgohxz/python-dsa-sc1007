

#
# creating a dict - mutable object
#
d = {'test': 'test', 'hello': [1, 2, 3]}

# creates a shallow copy
# shallow copy can be created from list slicing too
d2 = d.copy()

# modifiying an immutable element (string)
d2['test'] = 'bye'


def option1():
    # assigning a new mutable element (list)
    # note: this will not update the original dict since its simply pointing to a new memory containing a new list,
    # instead of modifying the existing one
    d2['hello'] = [6, 6, 6]
    print(d)  # {'test': 'test', 'hello': [1, 2, 3]} - not mutated
    print(d2)  # {'test': 'test', 'hello': [6, 6, 6]}


def option2():
    # will modify the original, since the list element is a mutable object
    d2['hello'][0] = 8
    print(d)
    print(d2)


option1()
# option2()
