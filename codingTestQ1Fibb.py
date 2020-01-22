
def printing(size):
"""program to print the first 12 even Fibonacci numbers"""
    count=0
    aaa=1
    bbb=1
    
    while count<size:
        
        ccc=aaa+bbb
        if(ccc%2==0):
            print(ccc)
            count+=1
        (aaa,bbb)=(bbb,ccc)    
        
        


def main():
    size=input("how many numbers?")
    size=int(size)
    printing(size)

#main starts from here
main()
