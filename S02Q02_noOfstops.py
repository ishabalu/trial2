

def noOfstops(distrav,totdis):
    count=0
    while(distrav>totdis ):
        count=count+1
        distrav=distrav-totdis
    print("the no of stops req is",count)
    
def calculate(svalue,evalue,fuel,tankcap,distrav=560):
    mil=(evalue-svalue)/fuel
    totdis=mil*tankcap
    noOfstops(distrav,totdis)

def main():
    svalue=input("what is the starting value of odometer?")
    svalue=int(svalue)
    evalue=input("what is the end value of odometer?")
    evalue=int(evalue)
    fuel=input("how much fuel used?")
    fuel=int(fuel)
    tankcap=input("what is the tank capacity of the car?")
    tankcap=int(tankcap)
    calculate(svalue,evalue,fuel,tankcap)
    

#main starts from here
main()
