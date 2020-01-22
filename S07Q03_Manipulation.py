sent=input("enter sentence")
size=len(sent)
print(sent[size-1])
print(sent[-5:])
print(sent[1],sent[4])
if(size%2==1):
    size=size-1
size=int(size/2)
print(str.upper(sent[size-1])+sent[size]+sent[size+1])
