# Rock Paper Scissors

# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

Symbol_ascii=[rock,paper,scissors]
Symbol_names=['rock','paper','scissors']
ch=int(input("""
Enter your Choice:
0-Rock
1-Paper
2-Scissor
"""))

import random
comp=random.randint(0,2)
print('computer chooses:',Symbol_ascii[comp],Symbol_names[comp])

print('You choose:',Symbol_ascii[ch],Symbol_names[ch])
if(comp==0):
    if(ch==1):
        print('you won')
    elif(ch==2):
        print('You loose')
    else:
        print('Draw')
elif(comp==1):
    if(ch==0):
        print('You loose')
    elif(ch==2):
        print('You won')
    else:
        print('Draw')
else:
    if(ch==0):
        print('You won')
    elif(ch==1):
        print('You loose')
    else:
        print('Draw')