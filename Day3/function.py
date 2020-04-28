def fact(a):
    f = 1
    for i in range(1,a+1):
        f = f*i
    return f


n = int(input())
c = fact(n)
d = fact(3)
e = fact(15)
print(c)
print(d)
print(e)