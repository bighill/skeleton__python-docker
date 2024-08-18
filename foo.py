import random

def guess_the_number():
  number_to_guess = random.randint(1, 10)
  user_guess = int(input("Pick a number between 1 and 10: "))

  if user_guess == number_to_guess:
      print("You guessed it! The number was indeed", number_to_guess)
  else:
      print("Sorry, that's not it. The number was", number_to_guess)

guess_the_number()
