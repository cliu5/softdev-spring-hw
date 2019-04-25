from functools import reduce

file=open('fairy.txt','r')
straw=file.read().replace(",","").replace(".","").replace(";","").replace("!","").replace("_","").replace(",","").replace("?","").strip()
#print(straw)

def wordFrequency(target):
    lines=straw.split(" ")
    #print(lines)
    count=[1 for word in lines if target.lower()==(word.lower())]
    #print(count)
    if len(count)!=0:
        return reduce((lambda a, b: a + b), count)

sample=['Once',' upon','time','time',]
def groupFrequency(target):
    lines=straw.split(" ")
    length=len(target.split(' '))
    count2=[lines[a:a+length] for a in range (0,len(lines)-length)]
    count3=[1 for part in count2 if ' '.join(part)==target]
    if len(count3)!=0:
        return reduce((lambda a, b: a+b),count3)
#print(wordFrequency('i'))
#print(groupFrequency('i'))

def mostWord():
    lines=straw.split(" ")
    words=[[target,wordFrequency(target)] for target in lines]
    for i in words:
        if i[1]==None:
            i[1]=0
    x= lambda a,b: a if a[1]>b[1] else b
    ans=(reduce(x,words))
    return ans[0]

x=mostWord()
print(x)
