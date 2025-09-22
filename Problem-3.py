a = int(input("enter a: "))
n = a if a%2 else a-1
series = [(2*i)-1 for i in range(1,n+1)]
res = ", ".join(map(str, series))
print(res)