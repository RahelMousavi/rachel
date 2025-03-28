"این کد اعدادی که سه گانه ی فیثاغورثی تشکیل میدهند را برمیگرداند."

def AreCoprime(m, n):
    def gcd(a, b):
        while(b):
            a, b = b, a % b
        return a

    if gcd(m, n) == 1:
        return True
    else:
        return False

def IsEven(m):
    if m%2 == 0 :
        return True
    else:
        return False

def IsOdd (n):
    if n%2 != 0:
        return True
    else:
        return False

def Biger(m,n):
    if m>n :
        return m , n
    elif n>m:
        return n , m
    else:
        return False

def A(m,n):
    a = m**2 - n**2
    return a

def B(m,n):
    b = 2*m*n
    return b

def C(m,n):
    c = m**2 + n**2
    return c

def pythagorean (m,n):
    flag =False
    if IsOdd(m) and IsEven(n):
        if AreCoprime(m,n):
            flag = True
    elif IsOdd(n) and IsEven(m):
        if AreCoprime(m,n):
            flag = True
    else:
        return False
    if flag:
        biger , smaller = Biger(m,n)
        a = A(biger , smaller)
        b = B(biger , smaller)
        c = C(biger , smaller)

    else:
        return False
    return a , b , c

def FindeingMN(n):
    temp ={}
    for i in range(1,n+1):
        for j in range(1,n+1):
            if pythagorean(i,j):
                temp[i] = j
            else:
                continue
    return temp

def ReturnC(d):
    temp = []

    for k,v in d.items():
        c = pythagorean(k,v)
        C = list(c)
        temp.append(C)

    return temp

def main():
    x = int(input("enter an number :"))
    mn = FindeingMN(x)
    print(f'all natural numbers from 1 to {x} that can make a Pythagorean Triplet are :',mn)
    list = ReturnC(mn)
    print(f'a, b , c will be :',list)

main()