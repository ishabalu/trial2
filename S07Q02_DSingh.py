name=input("name?")
surname=input("surname?")
size=len(surname)
size=size-1
print(str.capitalize(name[:-size]),str.capitalize(surname[:-size]))
