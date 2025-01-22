

#
# creating a dict - mutable object
#
d = {'test': 'test', 'hello': [1, 2, 3]}

# creates a shallow copy
d2 = d.copy()

# modifiying an immutable element (string)
# does not mutate the original variable 'd'
d2['test'] = 'bye'


def example1():
    # assigning a new mutable element (list)
    # note: this will not update the original dict since its simply pointing to a new memory containing a new list,
    # instead of modifying the existing one
    d2['hello'] = [6, 6, 6]

    print(d)  # {'test': 'test', 'hello': [1, 2, 3]} - not mutated
    print(d2)  # {'test': 'bye', 'hello': [6, 6, 6]}


def example2():
    # will modify the original, since the list element is a mutable object
    d2['hello'][0] = 8

    print(d)  # {'test': 'test', 'hello': [8, 2, 3]}
    print(d2)  # {'test': 'bye', 'hello': [8, 2, 3]}


# example1()
example2()
