d = int(input())

y = int(d/365)
d -= y * 365
m = int(d / 30)
d -= m * 30

print(repr(y)+" ano(s)")
print(repr(m)+" mes(es)")
print(repr(d)+" dia(s)")