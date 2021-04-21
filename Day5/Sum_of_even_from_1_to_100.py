#Method-1
sum_of_even=0
for i in range(0,101,2):
    sum_of_even+=i
print(f'Sum of even numbers from 0 to 100 is: {sum_of_even}')
#Method-2
sum_of_even=0
for i in range(0,101):
    if i%2==0:
        sum_of_even+=i
print(f'Sum of even numbers from 0 to 100 is: {sum_of_even}')
