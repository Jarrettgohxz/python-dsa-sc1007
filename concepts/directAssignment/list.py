l = [1, 2, 3, {'hello': 'test'}, [1, 2, 3]]
l2 = l


# all the operations on l2 will also mutate the original 'l' element
# all the operations on l will also mutate l2
l2[1] = 4
l2[3] = {'test': 'hello'}
l2[4] = [4, 5, 6]


print(l)  # [1, 4, 3, {'test': 'hello'}, [4, 5, 6]]
print(l2)  # 1, 4, 3, {'test': 'hello'}, [4, 5, 6]]
