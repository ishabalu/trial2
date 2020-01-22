num=input("enter a number")
num=int(num)
count=0
while num>0:
    count+=1
    num=num//10
print("no of digits:",count)    
