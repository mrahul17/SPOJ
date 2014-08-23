def PRIME1():
    a=[]
    b=[]
    t = int(input(''))
    for i in range(0,t):
        (m,n) = input('').split(' ')
        a.append((int(m),int(n)))
    for i in range(0,t):
        for j in range(a[i][0],a[i][1]+1):
            prime = 0
            for k in range(2,j):
                if j%k ==0:
                    prime = 1
                    break
            if (prime==0 and j!=1):
                b.append(j)
        for l in b:
            print(l)
        b=[]
        print('')
if __name__ == '__main__':
    PRIME1()
