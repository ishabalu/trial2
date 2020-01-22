import sys
def printing(count,num):
    print(num," *",count," =",num*count)

def main():
    num=sys.argv[1]
    num=int(num)
    til=int(sys.argv[2])
    count=1
    while(count<=til):
        printing(count,num)
        count=count+1

#main starts from here
main()
