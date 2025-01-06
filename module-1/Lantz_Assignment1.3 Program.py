# Author: Kypton Lantz
# Date: January 6, 2025
# Module 1.3 Assignment: Bottles of Beer
# This program will accept a user input for starting quantity of bottles, then count down to zero.

def main():
  #Display a welcome message
  print("Welcome to the Bottles of Beer Program!")

  try:
    #Get starting quantity from user
    bottles = int(input("To start, enter how many bottles there are: "))
    #Check for valid input (non-negative)
    if bottles < 0:
      print("The number of bottles cannot be negative. Please try again.")
  except ValueError:
    print("Invalid input. Please enter a numeric value.")

  #Print song lyrics and subtract 1 bottle until zero
  while bottles > 0:
    print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
    bottles = bottles - 1
    print(f"Take one down and pass it around, {bottles} bottle(s) of beer on the wall.")
  
  #Once zero is hit, remind user to buy more beer.
  print("Time to buy more bottles of beer.")

  #Display thank you message and close program
  print("\nThank you for using this program!\nHave a great day!")

#run the main function
if __name__ == "__main__":
  main()