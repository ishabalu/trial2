with open("testCopy.txt") as FH:
    count=0
    head=next(FH)
	for line in FH:
	    all_text=line.split(",")
	    if(count==5):
		break
	    print(all_text[1],all_text[0])
	    count+=1
