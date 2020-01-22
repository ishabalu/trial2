def inputing():
    num=int(input("number?"))
    return num
def check(num):
    count=0
    while num>0:
        count+=1
        num=num//10
    return count    

    

num=inputing()
single=0
two=0
three=0
counting=check(num)
if(counting==1):
    single+=1
elif(counting==2):
    two+=1
elif(counting==3):
    three+=1

maxi=num
mini=num

while num!=0:
    num=inputing()
    if(num>maxi):
        maxi=num
    elif(num<num):
        mini=num
    count=check(num)
    if(count==1):
        single+=1
    elif(count==2):
        two+=1
    elif(count==3):
        three+=1
print("one:",single,"two:",two,"three:",three)
print("max",maxi,"min",mini)
        
