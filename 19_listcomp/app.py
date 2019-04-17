'''
Team Clam Chowder -- Claire Liu and Maggie Zhao
SoftDev2 pd6
K19 -- PPFTLCW
'''
import math

def union(ary1,ary2):
    return [i for i in ary1] + [j for j in ary2 if j not in ary1]
print("============= Unions: =============")
print("Union of {1,2,3} and {2,3,4}")
print(union([1,2,3],[2,3,4]))
print("Union of {1,2,3} and {4,5,6}")
print(union([1,2,3],[4,5,6]))
print("Union of {1,2,3} and {1,2,3}")
print(union([1,2,3],[1,2,3]))

def intersection(ary1, ary2):
    return [i for i in ary1 for j in ary2 if i==j]
print("============= Intersections: =============")
print("Intersection of {1,2,3} and {2,3,4}")
print(intersection([1,2,3],[2,3,4]))
print("Intersection of {1,2,3} and {4,5,6}")
print(intersection([1,2,3],[4,5,6]))
print("Intersection of {1,2,3} and {1,2,3}")
print(intersection([1,2,3],[1,2,3]))

def setDiff(ary1,ary2):
    return [i for i in ary1 if i not in ary2]

print("============= Set Differences: =============")
print("Set Difference of {1,2,3} and {2,3,4}")
print(setDiff([1,2,3],[2,3,4]))
print("Set Difference of {1,2,3} and {4,5,6}")
print(setDiff([1,2,3],[4,5,6]))
print("Set Difference of {1,2,3} and {1,2,3}")
print(setDiff([1,2,3],[1,2,3]))
print("Set Difference of {1,2,3} and {2,3,4}")
print(setDiff([1,2,3],[2,3,4]))

def symDiff(ary1,ary2):
    return(setDiff(ary1,ary2)+setDiff(ary2,ary1))

print("============= Sym Differences: =============")
print("Sym Difference of {1,2,3} and {2,3,4}")
print(symDiff([1,2,3],[2,3,4]))
print("Sym Difference of {1,2,3} and {4,5,6}")
print(symDiff([1,2,3],[4,5,6]))
print("Sym Difference of {1,2,3} and {1,2,3}")
print(symDiff([1,2,3],[1,2,3]))
print("Sym Difference of {1,2,3} and {2,3,4}")
print(symDiff([1,2,3],[2,3,4]))

  
def cartesianProduct(ary1, ary2):
    return [(a, b) for a in ary1 for b in ary2]

print("============= Cartesian Product: =============")
print("Cartesian Product of {1,2} and {red, white}")
print(cartesianProduct([1,2],["red", "white"]))

