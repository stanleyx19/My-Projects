import random
import string

#This function is the password generator
def generatePassword(minLen, numbers = True, specialChar = True):
  
  letters = string.ascii_letters #grab all the ascii values of the letters
  digits = string.digits #grab all the digits
  specials = string.punctuation #grab the special characters such as @!$

  characters = letters 
  if numbers: #if we want numbers in our password
    characters += digits

  if specialChar: #if we want special characters in our password
    characters += specials

  password = ""
  meetsCriteria = False
  hasNums = False
  hasSpecials = False

  while not meetsCriteria or len(password) < minLen: #looping until we meet the criteria
    newChar = random.choice(characters) #Retrieve a random character from the character list
    password += newChar

    if newChar in digits: #Check if the new character added to the password is a digit
      hasNums = True

    elif newChar in specials: #Check if the new character added to the password is a special character
      hasSpecials = True

    meetsCriteria = True
    if numbers: #if the password has numbers
      meetsCriteria = hasNums

    if specialChar: #if the password has special characters
      meetsCriteria = meetsCriteria and hasSpecials #continues even if the previous if statement is True

  return password

if __name__ == "__main__":

  #This is our menu
  minLen = int(input("Enter the minimum length: "))
  hasNums = input("Do you want to have numbers? Press y for yes or n for no. ").lower() == "y"
  hasSpecials = input("Do you want to have special characters? Press y for yes or n for no. ").lower() == "y"

  #Getting our generated password
  password = generatePassword(minLen, hasNums, hasSpecials)
  print(f"Your generated password is: {password}")