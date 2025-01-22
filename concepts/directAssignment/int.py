i = 3
t = i

# does not mutate original variable 'i'
# int are NOT mutable (immutable)
t += 1

print(i)  # 3
print(t)  # 4
