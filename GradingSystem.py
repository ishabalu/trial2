def grade(percent):
    if(90<=percent<=100):
        print("First Class")
    elif(75<=percent<=89):
        print("Second Class")
    elif(percent<=35):
        print("Failed")
    else:
        print("Average")

def calculate(marks,total):
    studmarks=marks[0]+marks[1]+marks[2]
    percentage=(studmarks/total)*100
    return percentage

def inputing():
    studeng=input("what is your english marks out of 80?")
    studeng=int(studeng)
    studsci=input("what is your science marks out of 90?")
    studsci=int(studsci)
    studmath=input("what is your math marks out of 100?")
    studmath=int(studmath)
    return studeng,studsci,studmath
    

def main():
    eng=80
    sci=90
    math=100
    total=eng+sci+math
    marks=inputing()
    percentage=calculate(marks,total)
    grade(percentage)


#main starts here
main()
