from functools import reduce

file=open('fairy.txt','r')
straw=file.read().replace(",","").replace(".","").replace(";","").replace("!","").replace("(","").replace(")","").strip()
lines=straw.split(" ")
#print(lines)

def wordFrequency(target):
    count=[1 for word in lines if target.lower()==(word.lower())]
    #print(count)
    if len(count)!=0:
        return reduce((lambda a, b: a + b), count)
    
def groupFrequency(target):
    length=len(target)
    print(length)
    count2=[wordFrequency(word) for word in lines]
    if len(count)!=0:
        return reduce((lambda a, b: a+b), count2)

#print(wordFrequency('i'))
print(groupFrequency('i'))
