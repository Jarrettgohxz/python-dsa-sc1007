d = {'test': 'test', 'hello': [1, 2, 3]}
d2 = d.copy()


d2['test'] = 'bye'
d2['hello'] = [6, 6, 6]
# d2['hello'][0] = 8
print(d)
print(d2)

l = [1, 2, 3]
l2 = l.copy()

# l2 = [6,6,6]
l2[2] = 4

print(l)
print(l2)
