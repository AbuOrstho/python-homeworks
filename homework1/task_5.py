def reverse(x, a=0):
    f = 0
    if x == 0:
        f = a
    else:
        f = reverse(x // 10, a * 10 + x % 10)
    return f
assert (int(reverse(1000))) == 1
assert (int(reverse(142522))) == 225241
assert (int(reverse(104))) == 401
assert (int(reverse(10001))) == 10001
assert (int(reverse(111111111))) == 111111111
assert (int(reverse(101010101010000000000000000))) == 10101010101