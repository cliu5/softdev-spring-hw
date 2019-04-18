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

sample=['Once',' upon',' a ','time','time','a']
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
    words=[(target,wordFrequency(target)) for target in lines]
    return reduce((lambda a: t if words[1],words
    return words

x=mostWord()
print(x)
