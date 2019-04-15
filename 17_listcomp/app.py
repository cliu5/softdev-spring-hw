'''
Team coolgorlz -- Cathy Cai and Claire Liu
SoftDev2 pd8
K17 -- PPFTLCW
'''


import math

def Q1_loop():
    result = []
    for i in range (5):
        result.append(str(i * 22))
    return result

def Q1_list():
    return [str(i * 22) for i in range(5)]

def Q2_loop():
    ary=[]
    for i in range(5):
        ary.append(i*10+7)
    return ary

def Q2_list():
    return [i*10+7 for i in range(5)]

def Q3_loop():
    result = []
    for i in range(3):
        for j in range(3):
            result.append(str(i * j))
    return result

def Q3_list():
    return [str(i * j) for i in range(3) for j in range(3)]

def Q4_loop():
    ary=[]
    for x in range(101):
        for y in range(2, int(math.sqrt(x))+1):
            if (x%y ==0):
                ary.append(x)
                break
    return ary

def Q4_list():
    return [x for x in range(101) if len([1 for y in range(2, int(math.sqrt(x))+1) if x%y==0])!=0]

def Q5_loop():
    result = []
    for i in range(2, 101):
        p = 0
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i % j == 0):
                p += 1
        if p == 0:
            result.append(i)
    return result


def Q5_list():
    return [i for i in range(2,101) if i not in Q4_list()]

def Q6_loop(n):
    ary=[]
    for i in range(1,n):
        if(n%i==0):
            ary.append(i)
    return ary

def Q6_list(n):
    return [i for i in range(1,n) if n%i==0]

def Q7_loop(matrix):
    ary=[]
    for x in range(len(matrix[0])):
        ary.append([])
        for y in range(len(matrix)):
            ary[x].append(matrix[y][x])
    return ary

def Q7_list(matrix):
    return [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]



print(Q1_loop())
print(Q1_list())
print(Q2_loop())
print(Q2_list())
print(Q3_loop())
print(Q3_list())
print(Q4_loop())
print(Q4_list())
print(Q5_loop())
print(Q5_list())

n = 360
print(Q6_loop(n))
print(Q6_list(n))

matrix = [[0,0,0],[1,2,3],[4,4,5]]
print(Q7_loop(matrix))
print(Q7_list(matrix))
