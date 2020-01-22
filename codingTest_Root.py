"""print square root of postive 3 digit number"""
def root(aaa):
    print(aaa**0.5)
    inputing()
    
def check(num):
    aaa=num
    count=0
    while num>0:
        count+=1
        num=num//10
    if(count==3):
        root(aaa)
    else:
        inputing()
        

def inputing():
    num=int(input("enter number"))
    
    if num!=0:
        check(num)
        

def main():
    inputing()
    
#main starts from here
main()
