import math
def TETRA():
    all_tuple=[]
    n = int(input(''))
    for i in range(0,n):
        side_tuple = input('').split(' ')
        for k in range(0,6):
            side_tuple[k] = int(side_tuple[k])
        all_tuple.append(side_tuple)
    for j in range(0,n):
            U = all_tuple[j][3]
            V = all_tuple[j][4]
            W = all_tuple[j][5]
            u = all_tuple[j][2]
            v = all_tuple[j][1]
            w = all_tuple[j][0]
            X = (w-U+v)*(U+v+w)
            x = (U-v+w)*(v-w+U)
            Y = (u-V+w)*(V+w+u)
            y = (V-w+u)*(w-u+V)
            Z = (v-W+u)*(W+u+v)
            z = (W-u+v)*(u-v+W)
            a = math.sqrt(x*Y*Z)
            b = math.sqrt(y*Z*X)
            c = math.sqrt(z*X*Y)
            d = math.sqrt(x*y*z)
            volume = math.sqrt((-a+b+c+d)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d))/(192*u*v*w)
            s1 = (U+V+W)/2
            s2 = (U+v+w)/2
            s3 = (V+u+w)/2
            s4 = (W+u+v)/2
            A1 = math.sqrt(s1*(s1-U)*(s1-V)*(s1-W))
            A2 = math.sqrt(s2*(s2-U)*(s2-v)*(s2-w))
            A3 = math.sqrt(s3*(s3-V)*(s3-u)*(s3-w))
            A4= math.sqrt(s4*(s4-W)*(s4-u)*(s4-v))
            R = 3* volume/(A1+A2+A3+A4)
            print('{0:.4f}'.format(R))
            
if __name__ == '__main__':
    TETRA()
