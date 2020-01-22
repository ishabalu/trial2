sent=input("sentence")
size=len(sent)
count=0
wordcount=0
while(count<size):
    if(sent[count]==" "):
        wordcount+=1
        count+=1
    else:
        count+=1
count=0
acount=0

while(count<size):
  
    if(sent[count]=="a"):
        count+=1
        acount+=1
    else:
        count+=1        
        
print("word count",wordcount+1)
print("A words",acount)

