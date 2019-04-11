upper="ABCDEFGHIJKLMNOPQRSTUVWYZ"
lower="abcdefghijklmnopqrstuvwyz"
numbers="1234567890"
def minThreshold(pwd):
    a=[1 for x in upper if x in pwd]
    b=[2 for x in lower if x in pwd]
    c=[3 for x in numbers if x in pwd]
    d=a+b+c
    print(d)
    for i in d:
        if i==1:
            counterUpper+=1
        elif i==2:
            counterLower+=1
        elif i==3:
            counterNumber+=1
    if counterUpper!=0 and counterLower!=0 and counterNumber!=0:
        return True
    return False
minThreshold('ASDFasdfr234')
