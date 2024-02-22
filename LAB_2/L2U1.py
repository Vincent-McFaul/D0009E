import math

def bounce2(n):
    for i in range(n,-n-1,-1):
        print(abs(i))
        
def bounce(n):
    if n == 0:
        print(n)
        return
    print(n)
    bounce(n-1)
    print(n)    

def tvarsumman(n):
    if n < 10:
        return n 
    else: 
        return (n % 10) + int(tvarsumman(n / 10))

def tvarsumman2(n):
    tSumma = 0
    while n > 0:
        tSumma = int(tSumma + (n % 10))
        n = n / 10
    return tSumma

def derivative(f, x, h):
    tangentx = (1/(2*h)) * (f(x+h)-f(x-h))
    return tangentx

def funkInput(x):
    return x**2-1

def solve(f, x0, h):
    lastX = x0
    nextX = lastX + 10*h
    while (abs(lastX - nextX) > h): 
        lastX = nextX
        nextX = lastX - f(nextX) / derivative(f, lastX, h) 
    return nextX

#bounce2(4)
#bounce(4)   
#print(tvarsumman(24))
#print(tvarsumman2(24))
#print(derivative(math.sin, 1.57, 0.01))
print(solve(funkInput, 3, 0.0001))

import d0009e_lab2_bounceTest1
import d0009e_lab2_solveTest1
import d0009e_lab2_sumTest1
