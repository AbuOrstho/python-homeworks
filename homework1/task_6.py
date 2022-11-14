def unpack(f):
    x = str(f)
    s = '1234567890'
    n = ''
    for i in x:
        if i in s:
            n += i + ','
    L = [n[:-1]]
    return list(map(int, L[0].split(',')))


print(unpack( [0,0,[[1,2],-1,-2],5,6] ))
assert(unpack( [[1,3],4,5]  )) == [1,3,4,5]
assert(unpack( [0,0,[[1,2],-1,-2],5,6] )) == [0, 0, 1, 2, -1, -2, 5, 6]
assert(unpack( [[[[[[[1]]]]]]] )) == [1]
assert(unpack( [1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]] )) == [1,2,3,4,5,6,7,8,9]
