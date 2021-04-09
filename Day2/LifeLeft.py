# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rem_years=90-int(age)
print('You have',rem_years*365,'days,',rem_years*52,'weeks, and',rem_years*12,'months left' )

#using f-strings
rem_days=rem_years*365
rem_weeks=rem_years*52
rem_months=rem_years*12
print(f'You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left' )



"""

## Your Life in Weeks

# Instructions


Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old. 

It will take your current age as the input and output a message with our time left in this format:

> You have x days, y weeks, and z months left. 

Where x, y and z are replaced with the actual calculated numbers. 

 

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops. 

# Example Input

```
56
```

# Example Output

```
You have 12410 days, 1768 weeks, and 408 months left.
```

# Hint

1. There are 365 days in a year, 52 weeks in a year and 12 months in a year.
2. Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.

"""
