print("WELCOME TO THE PERCENTAGE CALCULATE")


while True:

    try:

        obtain_Marks = int(input("enter here your obtain marks :"))
    

        total_Marks = int(input("enter the total marks here :"))

        if total_Marks == 0:

            print("if you put zero it,s not valid please again enter nummber ")
            continue

        break

    except ValueError:
        print("please enter the valid number formate")


user = obtain_Marks/total_Marks*100

print(user)
