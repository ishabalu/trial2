import random
a=random.randint(1,25)
print(a)
def end():
    exit()
count=0
num=int(input("enter"))
if(num==a):
    print("welcome")
    exit()
else:
    print("invalid")
while(num!=a and count<3):
    num=int(input("enter"))
    if(num==a):
        end()
        break
    elif(count==2):
        print("hi")
    else:
        print("invalid")
        count+=1


    
