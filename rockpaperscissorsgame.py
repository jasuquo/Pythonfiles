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

game_image = [rock,paper,scissors]
choice = int(input("what do you chose,0 for  rock, 1 for  paper or 2 for scissors: "))
if choice >= 3 or choice  < 0:
  print("your number is invalid, you loose")
else:
  print(game_image[choice])
  # user_pick =["rock","paper","scissors"]
  computer_choice=random.randint(0,2)
  print ("computer choose:")
  print(game_image[computer_choice])
  
  print(f"\nYou chose {choice}, computer chose {computer_choice}.\n")
  
  if choice == computer_choice:
      print(f"Both players selected {choice}. It's a tie!")
  elif choice == 0:
      if computer_choice == 2:
          print("Rock smashes scissors! You win!")
      else:
          print("Paper covers rock! You lose.")
  elif choice == 1:
      if computer_choice == 0:
          print("Paper covers rock! You win!")
      else:
          print("Scissors cuts paper! You lose.")
  elif choice == 2:
      if computer_choice == 1:
          print("Scissors cuts paper! You win!")
      else:
          print("Rock smashes scissors! You lose.")
