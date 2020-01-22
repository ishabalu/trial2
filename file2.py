with open("testCopy.txt") as FH:
    count=0
    head=next(FH)
    for line in FH:
        alltxt=line.split(",")
        if(count==5):
            break
        print(alltxt[1],alltxt[0])
        count+=1
