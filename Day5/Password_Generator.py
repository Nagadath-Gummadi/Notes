alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
l=int(input('How many letters would you like in your password?:'))
n=int(input('How many numbers would you like in your password?:'))
s=int(input('How many symbols would you like in your password?:'))
import random
password=''
for i in range(l):
    password+=random.choice(alphabets)
for i in range(n):
    password+=random.choice(numbers)
for i in range(s):
    password+=random.choice(symbols)
print(f'Your password is: {password}')
pass_list=list(password)
random.shuffle(pass_list)
random_password=''
for i in pass_list:
    random_password+=i
print(f'Randomized password is: {random_password}')