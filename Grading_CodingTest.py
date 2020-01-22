""" Grading System """
def passcheck(eng,sciT,sciP,math,percentage,passpercent):
    if(eng>=25 and math>=35 and (sciT+sciP)>=35 and sciT>=25 and sciP>=8):
        grade(percentage,passpercent)
    else:
        print("fail")

        
def grade(percentage,passpercent):
    if(percentage>90):
        print("Grade A")
    elif(75<percentage<=90):
        print("Grade B")
    elif(percentage< passpercent):
        print("Fail")
    else:
        print("Average")

        
def calculate(eng,sciT,sciP,math,passpercent):
      Scimark=sciT+sciP
      total=eng+sciT+sciP+math
      percentage=(total/275)*100
      passcheck(eng,sciT,sciP,math,percentage,passpercent)
      

def inputing(passpercent):
    print("input marks ")
    
    eng=int(input("English"))
    sciT=int(input("Science Theory"))
    sciP=int(input("Science Practical"))
    math=int(input("Mathematics"))
  
    calculate(eng,sciT,sciP,math,passpercent)
   
def main():
    (Emax,STmax,SPmax,Mathmax)=(75,75,25,100)
    Science=SPmax+STmax

    (Epass,STpass,SPpass,Sciencepass,Mathpass)=(25,25,8,35,35)
    passpercent=((Epass+Sciencepass+Mathpass)/275)*100
    inputing(passpercent)
#main starts from here
main()
