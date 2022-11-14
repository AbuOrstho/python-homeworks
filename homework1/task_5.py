def reverse_int(x, a=0):
    f = 0
    if x == 0:
        f = a
    else:
        f = reverse_int(x // 10, a * 10 + x % 10)
    return f

print(reverse_int(1111111))
assert(reverse_int(1000)) == 1
assert(reverse_int(142522)) == 225241
assert(reverse_int(104)) == 401
assert(reverse_int(10001)) == 10001
assert(reverse_int(111111111)) == 111111111
assert(reverse_int(101010101010000000000000000)) == 10101010101
