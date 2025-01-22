d = {'test': 'test', 'hello': [1, 2, 3], 'bye': [4, 5, 6]}


d3 = d

d3['test'] = 'bye'  # will update the original 'd' variable
d3['hello'] = [8, 8, 8]  # will update the original 'd' variable
d3['bye'][1] = '6'


print(d)  # {'test': 'test', 'hello': [8, 8, 8]}
print(d3)  # {'test': 'test', 'hello': [8, 8, 8]}
