'''
Team coolgorlz -- Cathy Cai and Claire Liu
SoftDev2 pd8
K17 -- PPFTLCW
'''

import math

def number2A():
    ary=[]
    for i in range(5):
        ary.append(x*10+7)
    return ary
    
def number2B():
    return [i*10+7 for i in range(5)]

def number4A():
    ary=[]
    for x in range(101):
        for y in range(2, int(math.sqrt(x))+1):
            if (x%y ==0):
                ary.append(x)
                break
    return ary

def number4B():
    return [x for x in range(101) if len([1 for y in range(2, int(math.sqrt(x))+1) if x%y==0])!=0]

print(number4B())

def number6A(n):
    ary=[]
    for i in range(1,n):
        if(n%i==0):
            ary.append(i)
    return ary

def number6B(n):
    return [i for i in range(1,n) if n%i==0]

def number7A(matrix):
    ary=[]
    for x in range(len(matrix[0])):
        ary.append([])
        for y in range(len(matrix)):
            ary[x].append(matrix[y][x])
    return ary

def number7B(matrix):
    return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]

