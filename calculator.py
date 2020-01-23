#ice is best
def add(num1,num2):
    sum = 0
    sum = num1 + num2
    return sum

def sub(num1,num2):
    diff = num1 - num2
    return diff

#main starts from here
alpha=10
beta=20
result=add(alpha,beta)
print("sum is ",result)
result=sub(alpha,beta)
print("the difference is",result)


eng1 = 250
ind1 = 220
eng2 = 180
etot = add(eng1, eng2)
india_need = sub(etot, ind1)
ind_target = add(india_need, 1)
print("need",ind_target,"to win")

veg = 120
fruits = 45
cash = 200
tot = add(veg, fruits)
cashback = sub(cash,tot)
print(" cash returned is",cashback)
