from math import *
def exp(n):
    a = 0
    for c in range(0,100):
        a += ((n)**c)/factorial(c)
    return a
        
def power(b,x):
    a = 0
    for c in range(0,1000):
        a+= (b**(c*x))/factorial(c)
    return log(a)

def interest(a,b):
    if a[1]=="i": 
        r = 0
        i = 0
        p = 1
        rTest = False
        iTest = False
        for g in range(0,b+1):
            if g >=1:
                p  = p*(1-(g-1)/b)
            if g%2==0:
                if rTest:
                    r -= ((a[0]**g)/factorial(g))*p
                else:
                    r += ((a[0]**g)/factorial(g))*p
                rTest = not rTest
            else:
                if iTest:
                    i -= ((a[0]**g)/factorial(g))*p
                else:
                    i += ((a[0]**g)/factorial(g))*p
                iTest = not iTest
        return [r,i]
    else:
        return([(1+(a[0]/b))**b,0])
    
def complex_multiply(a,b):
    c = [a[0]*b[0]-a[1]*b[1],a[0]*b[1]+b[0]*a[1]]
    a = c    
    return c

def complexEXP(a,b,l=False):
    h = a
    if l:
        print(str(a)[1:-1])    
    for c in range(0,b-1):
        h = complex_multiply(h,a)
        if l:
            print(str(h)[1:-1])
    return h
    
     
x = interest([1,"i"],2000)   
print(complexEXP([-0.62996052495,1.09112363597],3))
