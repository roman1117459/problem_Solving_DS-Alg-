
s = int(input())
h = int(s / 3600)
s -= h * 3600
m = int(s /60)

s -= m * 60



print(repr(h)+":"+repr(m)+":"+repr(s))
