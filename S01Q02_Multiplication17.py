def printing(count,num):
    print(17," *",count,"=",17*count)

def main():
    num=input("what num do you want mul table for?")
    num=int(num)
    count=1
    while(count<=10):
        printing(count,num)
        count=count+1

#main starts from here
main()
