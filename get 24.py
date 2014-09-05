'''
Riddle:
Using only the four elementary operations: +, - , *, /;
and the numbers 1, 3, 4, 6
you need to obtain 24

The aim of this code is to show that the solution is unique.
(Try to find the solution without running this code!)
'''
def op(a,b,i):
    if i==1:
        return(a+b);
    elif i==2:
        return(a-b);
    elif i==3:
        return(a*b);
    elif i==4:
        if b!=0:
            return(a/b);
        else:
            return 1000
A=[1.0,3.0,4.0,6.0];  #It's important to declare all the variables as float, otherwise 1/3=0 for example.
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for x in A:
                for y in A:
                    if x!=y:
                        for z in A:
                            if x!=z and y!=z:
                                for w in A:
                                    if x!=w and y!=w and z!=w:
                                        a=op(op(op(x,y,i),z,j),w,k)
                                        b=op(op(x,y,i),op(z,w,j),k)
                                        c=op(x,op(y,op(z,w,i),j),k)
                                        d=op(x,op(op(y,z,i),w,j),k)
                                        e=op(op(x,op(y,z,i),j),w,k)
                                        if a==24.0:
                                            print [x,y,z,w,i,j,k,1]
                                        if b==24.0:
                                            print [x,y,z,w,i,j,k,2]
                                        if c==24.0:
                                            print [x,y,z,w,i,j,k,3]
                                        if d==24.0:
                                            print [x,y,z,w,i,j,k,4]
                                        if e==24.0:
                                            print [x,y,z,w,i,j,k,5]