import math
number=int(input("number?"))
count=1
while count<150:
    square=math.pow(count,2)
    if(square<number):
        print(square)
    else:
        break
    count+=1
    
