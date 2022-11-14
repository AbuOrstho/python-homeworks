def foo(a,b):
    f = []
    n = (a + b)
    if len(a) == len(b):
        f = sorted([a*b for a,b in zip(a,b)])
    else:
        f = sorted([j for j in n if n.count(j) > 1])
    return f



assert(foo([1, 2, 3, 3, 3], [-1, 2, 3])) == [2, 2, 3, 3, 3, 3]
assert(foo( [1, 2, 3],[-1, 2, 0])) == [-1,0,4]
assert(foo([0,0,1, 0, 11, 8, 9], [-1,-2,-3,-4,-5,-7])) ==[0,0,0]
