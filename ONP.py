def ONP():
    arr=[]
    out=[]
    queue=[]
    t = int(input(''))
    for i in range(0,t):
        arr.append(input(''))
    for i in range(0,t):
        ex = arr[i]
        for j in ex:
            if j in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                out.append(j)
            if j in ['+','-','*','/','^']:
                queue.append(j)
            if (j=='('):
                queue.append(j)
            if(j==')'):
                while(queue[-1]!='('):
                    out.append(queue.pop())
                if(queue[-1]=='('):
                    queue.pop()
            
        print(''.join(out))
        out=[]
        queue=[]
        
if __name__=='__main__':
    ONP()
