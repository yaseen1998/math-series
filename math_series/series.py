

def fibonacci(n): # declare fibonacci function 
    """ Fibonacci sequence, such that each number is the sum of the two preceding ones,
    starting from 0 and 1. That is"""
    if n==0: # first number of fibonacci it is 0
        return 0
    if n==1: # second number of fibonacci it is 1
        return 1
    else: # 
        return fibonacci(n-1)+ fibonacci(n-2)

for i in range(8):
    print(fibonacci(i))

def lucas(n): # declare fibonacci lucas 
    """ lucas sequence, such that each number is the sum of the two preceding ones,
    starting from 2 and 1. That is"""
    if n== 0:# first number of fibonacci it is 2
        return 2
    if n== 1:# second number of fibonacci it is 1
        return 1
    else:
        return lucas(n-1)+ lucas(n-2)

for i in range(8):
    print(lucas(i))
# 4
# fib3+ fib2
# fib2+fib1
# fib1+fib0
# 1+0+1+1+0=3
def sum_series(n,i=0,j=1):
    """ sum_series function it's return a  Fibonacci sequence in default i,j 
    of you change the default i,j then you change the first two number"""
    if n==0:
        return i
    if n==1:
        return j
    else:
        return sum_series(n-1,i,j)+ sum_series(n-2,i,j)

# for i in range(8):
print(sum_series(7,2,1))