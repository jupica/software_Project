# defining the variables that describe the death
poisoned = "It turns out to be poisonous. You die."
dehydrated = "You decide not to drink from the pool, You die from dehydration"
pit = "You go through door 3. Behind it you find... a bottomless pit, you fall to your death."

def game():
  direction = 0
  score = 0 # Initialise score as 0
# print welcome message into console
  print("Welcome to my choose your own adventure story")
# asks user for the first input, storing the value in a variable "answer"
  answer = input("Let\'s begin!\nThere are three doors. Which door do you go through? Type '1', '2', or '3': ")
# checks if the variable "answer" contains the value "1"
  if answer == "1":
    # set path to match answer direction
    direction = 1
# checks if the variable "answer" contains the value "2"
  elif answer == "2":
    direction = 2
  elif answer == "3":
    print(pit)
    score += 0
    direction = 0
    replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
    if replay == "y":
      game()
    elif replay =="n":
      return
    else:
      replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")

  if direction == 1:
    # asks user for another value, which replaces the previous value in "answer"
    answer = input("You go through door 1. Behind it you find... a field of purple mushrooms.\nType '1' to eat one, type '2' to ignore them and continue walking: ")
    direction = int(answer)
  elif direction == 2:
    # asks user for another value, which replaces the previous value stored in "answer"
    answer = input("You go through door 2. Behind it you find... a single apple tree in a field.\nType '1' to eat an apple, type '2' to ignore the tree and continue walking: ")
    direction = int(answer)

  if direction == 1:
    # prints "poisoned" (defined earlier)
    print(poisoned)
    # increases score
    score += 50
    direction = 0
    # asks user if they want to replay, and displays score
    replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
    # check if user inputted 'y'
    if replay == "y":
      # starts game again
      game()
      return
    # check if the user inputted 'n'
    elif replay =="n":
      # exits game
      return
      # if other conditions arent met
    else:
      # ask again
      replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
  elif direction == 2:
    # asks the user for another value, which replaces the previous value in "answer"
        answer = input("You walk through the field, and find a pool.\nRealising you are thirsty, do you take a drink? Type '1' to drink, type '2' to not drink: ")
    direction = int(answer)
    
  if direction == 1:
    # prints message to console telling the user they completed the game
    print("You drink the water, and feel refreshed. You finished my game without dying, Good Job")
    score += 100
    direction = 0
    replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
    if replay == "y":
      game()
    elif replay =="n":
      return
    else:
      replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
  elif direction == 2:
    # prints "dehydrated" (defined earlier)
    print(dehydrated)
    score += 75
    print(f'{score/100} completed!')
    replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
    if replay == "y":
      game()
    elif replay =="n":
      return
    else:
      replay = input(f"You got a score of {score}/100.\nPlay again? Type 'y' to replay, type 'n' to quit")
#--------------------------------------------------------#


game()
