n,m = [int(i) for i in input().split()]
def exp(n):
    if n==1:
        return 3%m
    mod = exp(n//2)
    mod = (mod*mod)%m
    if n%2!=0:
        mod = (mod*3)%m
    return mod
r = exp(n)-1
print(r if r != -1 else m-1)