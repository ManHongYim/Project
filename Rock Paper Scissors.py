import random

print("Instruction: \nHere is a little rock paper scissors game,\n"
      "you can choose randomly from rock(R), paper(P) or scissors(S),\n"
      "and the computer will do the same.\n"
      "The rules is that: Rock wins scissors, paper wins rock, scissors wins paper,\n"
      "Good Lcuk and have fun!!\n")
print('If you want leave the game, just enter quit!')
choices = ['r','s','p']
def is_win(your_action, computer_action):
      if your_action =='r' and computer_action == 's':
            return True
      elif your_action == 'p'and computer_action == 'r':
            return True
      elif your_action == 's' and  computer_action == 'p':
            return True
      else:
            return False
def choice(x):
      if x == 'r':
           return 'Rock'
      elif x == 'p':
           return 'Paper'
      elif x == 's':
           return 'Scissors'
while True:
      action = input('Enter your action(Rock(R), Paper(P), Scissors(S):').lower()
      if action == 'quit':break
      try:
            assert action in choices
      except:
            print('Invalid input')
            continue
      robot = random.choice(choices)
      if is_win(action, robot):
            print(f"Your action:{choice(action)}")
            print(f"Robot's action:{choice(robot)}")
            print('Congrat!, You won!')
      elif action == robot:
            print(f"Your action:{choice(action)}")
            print(f"Robot's action:{choice(robot)}")
            print('Tie!, Try again!')
      else:
            print(f"Your action:{choice(action)}")
            print(f"Robot's action:{choice(robot)}")
            print('Sorry, You lose! Try again!')


