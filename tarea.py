import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

piedra_papel_tijeras=['rock','paper','scissors']
computer_random_number=random.randint(0,2)
computer=piedra_papel_tijeras[computer_random_number]
answer_user=int(input('Elige un numero del 0 al 2: '))
user=piedra_papel_tijeras[answer_user]
print(f'Tu elegiste: {user} y la computadora eligio: {computer}')
if answer_user == 2 and computer_random_number ==1:
    print(scissors)
if answer_user==1 and computer_random_number==0:
    print(paper)
if answer_user==0 and computer_random_number==1:
    print(paper)