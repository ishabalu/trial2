def add(num1,num2):
    sum = 0
    sum = num1 + num2
    return sum

def sub(num1,num2):
    diff = num1 - num2
    return diff

#main starts from here
if __name__=="__main__":
    alpha=10
    beta=20
    result=add(alpha,beta)
    print("sum is ",result)
    result=sub(alpha,beta)
    print("the difference is",result)
    

