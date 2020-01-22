def  do_1digit_oper(number):
    aaa=number+7
    print(aaa%10)
    
def  do_2digit_oper(number):
    bbb=number**5
    print(bbb%10)

def operation1(count,number):
    if(count==1):
        do_1digit_oper(number)
    elif(count==2):
        do_2digit_oper(number)
    elif(count==3):
        inputing(number)
        
def do_3digit_oper(num1,num2):
    result=num1+num2
    print(result%10)

def check(number):
    keepnumber=number
    count=0
    while(number>0):
        count=count+1
        number=int(number/10)
    return count
def inputing(number):
    num1=input("enter another number")
    num1=int(num1)
    do_3digit_oper(number,num1)
    


def main():
    num=input("enter a number")
    num=int(num)
    count=check(num)
    operation1(count,num)

#main starts here
main()
