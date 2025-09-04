def Factorial(n):
    # if(n==1 or n==0):
    #     return 1
    # else:
    #     return n*Factorial(n-1)
    f=1
    for i in range(2,n+1):
        f*=i
    return f
    

def Combination(n,r):
    C=int(Factorial(n)/(Factorial(r)*Factorial(n-r)))
    return C


n=int(input('Enter the size of the triagle : '))
i=0
while(i<n):

    #space
    j=n
    while(j>=i):
        print(end=' ')
        j-=1
    
    #for pattern
    k=0
    while(k<=i):
        print(Combination(i,k),end=' ')
        k+=1
        
    print()
    i+=1