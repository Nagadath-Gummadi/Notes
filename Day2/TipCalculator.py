#If the bill was $150.00, split between 5 people, with 12% tip. 
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill=float(input('Enter the bill amount: '))
n=int(input('Enter number of persons: '))
tip=float(input('Enter the tip percent: '))

round_tip=(bill+((bill*(tip/100))))/n
#tip_as_percent = tip / 100
#total_tip_amount = bill * tip_as_percent
#total_bill = bill + total_tip_amount
#bill_per_person = total_bill / people

print('Everyone should pay:',round(round_tip,2))

