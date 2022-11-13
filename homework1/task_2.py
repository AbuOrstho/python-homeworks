def from_list_to_dict(a):
    b = {}
    con = 0
    for i in a:
        for j in a:
            if i == j:
                con += 1
        b[i] = con
        con = 0
    return b

assert(from_list_to_dict([1])) == {1:1}
assert(from_list_to_dict([0, 0, 0, 0])) == {0:4}
assert(from_list_to_dict([1,2,3,1,3,5] )) == {2:1, 1:2, 3:2, 5:1}
assert(from_list_to_dict([1, -1, 1.1, 1.1, 10, 100, 100, 100])) == {1:1, -1:1, 1.1:2, 10:1, 100:3}




