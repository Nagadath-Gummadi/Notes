height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi=int(float(weight)/(float(height)**2))
print(f'your bmi is: {bmi}')
if(bmi<18.5):
    print('under-weight')
elif(bmi<25 and bmi>18.5):
    print('normal-weight')
elif(bmi<30 and bmi>25):
    print('over-weight')
elif(bmi<35 and bmi>30):
    print('obese')
else:
    print('clinically obese')