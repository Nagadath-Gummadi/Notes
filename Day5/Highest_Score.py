students_mark=input('Enter students marks seperated by ",":')
marks=students_mark.split(',')
print(marks)
max_of_marks=0
for mark in marks:
    if int(mark)>max_of_marks:
        max_of_marks=int(mark)
print('Highest mark among all the students is:',max_of_marks)