upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
nums="0123456789"
chars=".?!&#,;:-_*"

def minThresh(pwd):
    a= [1 for x in upper if x in pwd]
    b= [2 for x in lower if x in pwd]
    c= [3 for x in nums if x in pwd]
    ans=a+b+c
    thresh= (1 in ans and 2 in ans and 3 in ans)
    return thresh

def strengthOfpwd(pwd):
    strength=[0 if x in upper else 1 if x in lower else 2 if x in nums else 3 if x in chars else 4 for x in pwd]
    counter=0
    if 0 in strength:
        counter+=2.5
    if 1 in strength:
        counter+=2.5
    if 2 in strength:
        counter+=2.5
    if 3 in strength:
        counter+=2.5
    return counter


    
