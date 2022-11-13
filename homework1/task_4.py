import re

def l_substr(n):
    f = re.findall(r'(?=((.+?)\2+))', n)
    return max((l[0] for l in f), key=len, default='')


print(l_substr("aaabbbbbaabbccaaaaaaaaa"))



assert(l_substr("")) == ''
assert(l_substr("a")) == 'a'
assert(l_substr("aa")) == 'aa'
assert(l_substr("abb")) == 'bb'
assert(l_substr("hellloo worldd")) == 'lll'
assert(l_substr("aaabbbbbaabbccaaaaaaaaa")) == 'aaaaaaaaa'
assert(l_substr("4512451111111111111111111111111111111111111111111122222222222223333")) == '11111111111111111111111111111111111111111111'