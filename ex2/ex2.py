N=int(input("Please provide a number: "))
if N==1:
    print(N,"is not prime")
else:
    for i in range (1,N+1):
        #if i!=1 and i!=N and N%i==0:
        if i not in {1,N} and N%i==0:
            print(N,"is not prime")
            break
        else:
            if i==N-1:
                print(N,"is prime")
