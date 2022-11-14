def unpack(f):
    x = str(f)
    s = '[]'
    a = ''
    n = ''
    for i in x:
        if i in s:
            a += i + ','
        else:
            n += i
    r = ('[%s]' % ','.join(map(str, [n])))
    res_str = str(r).replace(", ", ',')
    return res_str




print(unpack( [0,0,[[1,2],-1,-2],5,6] ))
assert(unpack( [[1,3],4,5]  )) == [1,3,4,5]
assert(unpack( [0,0,[[1,2],-1,-2],5,6] )) == [0, 0, 1, 2, -1, -2, 5, 6]
assert(unpack( [[[[[[[1]]]]]]] )) == [1]
assert(unpack( [1,[2,[3,[4,[5,[6,[7,[8,[9]]]]]]]]] )) == [1,2,3,4,5,6,7,8,9]