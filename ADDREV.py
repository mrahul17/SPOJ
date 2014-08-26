def ADDREV():
    inputlist = []
    n = int(input(''))
    for i in range(0,n):
        num = input('').split(' ')
        numlist = (num[0][::-1],num[1][::-1])
        inputlist.append(numlist)
    for j in range(0,n):
        sum1 = str(int(inputlist[j][0])+int(inputlist[j][1]))[::-1]
        sum2 = sum1
        for ch in range(0,len(sum2)):
            if(sum2[ch]!='0'):
                break
            else:
                sum1 = sum2[ch+1:]
        print(sum1)
            
        
        
        

    

if __name__ == '__main__':
    ADDREV()
