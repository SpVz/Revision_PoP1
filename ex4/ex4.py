def fibonacci(N):
    if N==1:
        return 0
    if N in {2,3}:
        return 1
    else:
        return fibonacci(N-1)+fibonacci(N-2)
    
Num_fib=int(input("Please enter the number of fibonacci Numbers to be calculated: "))
fib_values=[]
for i in range (1,Num_fib+1):
    fib_values.append(fibonacci(i))
print(fib_values)
