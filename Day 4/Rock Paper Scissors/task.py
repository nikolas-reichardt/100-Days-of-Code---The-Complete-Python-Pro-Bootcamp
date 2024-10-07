import random
from turtledemo.sorting_animate import randomize

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

draw1 = random.randint(0,2)
print(draw1)
draw2 = int(input("What do you choose? Rock(0) Paper(1) Scissor(2): "))
print(f"You chose {draw2}.\n Your Opponent chooses:")

if draw1 == 0:
    print(rock)
elif draw1 == 1:
    print(paper)
else:
    print(scissors)

if draw1 == draw2:
    print("REPEAT!")
elif draw1 == 0 and draw2 == 1:
    print("YOU WIN")
elif draw1 == 0 and draw2 == 2:
    print("YOU LOOSE")
elif draw1 == 1 and draw2 == 0:
    print("YOU LOOSE")
elif draw1 == 1 and draw2 == 2:
    print("YOU WIN")
elif draw1 == 2 and draw2 == 0:
    print("YOU WIN")
elif draw1 == 2 and draw2 == 1:
    print("YOU LOOSE")
else:
    print("YOU WIN")
