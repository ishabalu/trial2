import random


def fun():
    num=inputing()
    check(num,0)
    
def inputing():
    num=int(input("Enter Passcode"))
    return num

def check(num,flag):
    counting=0
    if(num==a):
        print("Welcome!!!")
        exit()
    elif(num!=a and flag==1):
        print("Login FAILED")
        exit() 
    else:
        print("Invalid Passcode")
        return 
        

def lastTime(num):
    
    if(num+1==a or num+2==a or num-1==a or num-2==a):
        print("Invalid Passcode")
        number=inputing()
        check(number,1)
        
    else:
        print("Login FAILED")
        exit()


a=random.randint(1,25)
print(a)

def main():
    count=0
    while(count<3):
        fun()
        count+=1
    num=inputing()
    lastTime(num)
#main starts from here    
main()

    
