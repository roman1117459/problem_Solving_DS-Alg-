a = int(input())
print(a)
print("{} nota(s) de R$ 100,00".format(int(a/100)))
b = a % 100
print("{} nota(s) de R$ 50,00".format(int(b/50)))
b = b % 50
print("{} nota(s) de R$ 20,00".format(int(b/20)))
b = b % 20
print("{} nota(s) de R$ 10,00".format(int(b/10)))
b = b % 10
print("{} nota(s) de R$ 5,00".format(int(b/5)))
b = b % 5
print("{} nota(s) de R$ 2,00".format(int(b/2)))
b = b %2
print("{} nota(s) de R$ 1,00".format(int(b/1)))
