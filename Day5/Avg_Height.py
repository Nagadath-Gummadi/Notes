students_height=input('Enter students height seperated by ",":')
heights=students_height.split(',')
print(heights)
sum_of_heights=0
for height in heights:
    sum_of_heights+=int(height)
print('Average of students height is:',sum_of_heights/len(heights))