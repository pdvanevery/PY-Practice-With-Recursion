# Write code for algorithm 3 below
def fib_seq(n):
    if n == 0:
        return 0
    elif n <= 1:
        return n
    else:
        return fib_seq(n-1) + fib_seq(n-2)

for i in range(0,10):
    print(fib_seq(i))


#iterative-not done
def fibseq2(n):
    if n <= 1:
        return n 
    result = [0,1]
    for i in range(2, n+1):
        result.append(result[n-1] + result[n-2])
        return result[n]

for i in range(0, 10):
    print(fibseq2(3))    