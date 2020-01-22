def printing(mil):
    print("mileage is ",mil)

def calculate(svalue,evalue,fuel):
    mil=(evalue-svalue)/fuel
    printing(mil)
    


def main():
    svalue=input("what is the starting value of odometer?")
    svalue=int(svalue)
    evalue=input("what is the end value of odometer?")
    evalue=int(evalue)
    fuel=input("how much fuel used?")
    fuel=int(fuel)
    calculate(svalue,evalue,fuel)
    
#main starts from here
main()
