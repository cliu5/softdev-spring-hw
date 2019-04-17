from functools import reduce

file=open('fairy.txt','r')
straw=file.read().replace(",","").replace(".","").replace(";","").replace("!","").replace("(","").replace(")","").strip()
lines=straw.split(" ")

sample=['hi','asdf','bye','hi']

def wordFrequency(word):
    count=0
    for i in sample:
        if i==word:
            count+=1
    return(count)
step=0
word="hi"
print(reduce(lambda a: step+(1 if a.equals(word)),sample))
wordFrequency('hi')
