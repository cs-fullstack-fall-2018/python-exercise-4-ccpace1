grade=int(input("What is your numerical grade?"))

if(grade>100):
    print("You have too much extra credit...")
elif(grade>=90):
    print("You have an A")
elif(grade>=80):
    print("You have a B")
elif(grade>=70):
    print("You have a C")
elif(grade>=60):
    print("You have a D")
elif(grade>=0):
    print("You have an F")
else:
    print("You can't be negative!")