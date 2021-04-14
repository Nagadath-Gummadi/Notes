year=int(input(prompt='Enter an year:'))
if (year%4==0 ):
    if(year%100==0 and year%400==0):
        print('Given Year is a leap year')
    else:
        print('Given Year is not a leap year')
    print('Given Year is not a leap year')
else:
    print('Given Year is not a leap year')