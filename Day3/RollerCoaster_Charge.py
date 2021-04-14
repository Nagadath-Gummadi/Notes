print('Welcome to roller coaster')
height=int(input('Enter your height in cm:'))
if height>=160:
    print("Hey! you are eligible to this ride. Enjoy the day")
    age=int(input("Enter your age:"))
    if(age<18 and age>14):
        print("Your charge is 20 rupees.")
    elif(age<14 and age>12):
        print("Your charge is 15 rupees.")
    elif(age<12):
        print("Your charge is 10 rupees")
    else:
        print("Your charge is 25 rupees")
else:
    print("Oops! You are Not Eligible with this height.")