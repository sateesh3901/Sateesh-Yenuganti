a = int(input("enter a: "))
series = [(2*i)-1 for i in range(1,a+1)]
res = ", ".join(map(str, series))
print(res)
