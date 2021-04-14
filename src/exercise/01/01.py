import random

choice_options = {
  '1': 'ROCK',
  '2': 'PAPER',
  '3': 'SCISSORS'
}

choices = []
for v in choice_options.values():
  choices.append(v)

ai = random.choice(choices)
user = input('ROCK, PAPER, SCISSORS!!!!\nChoose Your Option...\n\n1. Rock\n2. Paper\n3. Scissors\n')

# 1. Define a function that takes in both choices
# 2. Return a boolean depending on if user wins
# 3. Define a function that returns string result based on win status
# 4. Print win result function

if user not in choices:
  print('You must choose either 1, 2, or 3 as an option.')

if ai == user:
  print('Tie!')
