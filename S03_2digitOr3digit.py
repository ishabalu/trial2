def check(number):
    keepnumber=number
    count=0
    while(number>0):
        count=count+1
        number=int(number/10)
    return count        

def printing(number,count):
    if(count==2):
        print(number,"is 2 digit")
    elif(count==3):
        print(number,"is 3 digit")
    else:
        print(number)
        

def main():
    num1=input("enter 1st number")
    num1=int(num1)
    num2=input("enter 2nd number")
    num2=int(num2)
    aaa=check(num1)
    bbb=check(num2)
    printing(num1,aaa)
    printing(num2,bbb)
    

#main starts from here
main()
