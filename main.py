_m = dict()
_p = dict()
_i = dict()
_s = input()
k1 = 0
k2 = 0
k3 = 0
while _s != '':
    s = _s.split()
    _m[s[0]+s[1]] = int(s[2])
    k1 = k1 + 1
    _s = input()

_s = input()
while _s != '':
    s = _s.split()
    _p[s[0]+s[1]] = int(s[2])
    k2 = k2 + 1
    _s = input()

_s = input()
while _s != '':
    s = _s.split()
    _i[s[0]+s[1]] = int(s[2])
    k3 = k3 + 1
    _s = input()

k = k1 + k2 + k3
print(k)
