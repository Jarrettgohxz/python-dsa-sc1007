# = y&& << ab >> c + de,


# STACK
# "d" (d)
# "e" "d" (e)
# "d+e" (+)
# "d+e" "c" (c)
# "c >> d+e" (>>)
# "c >> d+e" "b" (b)
# "c >> d+e" "b" "a" (a)
# "c >> d+e" "a<<b" (<<)
# "a<<b && c >> d+e" (&&)
# "a<<b && c >> d+e" "y" (y)
# "y = a<<b && c >> d+e" (=)
