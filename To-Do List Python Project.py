import random
import string

class Tasks:

    def __init__(self, description, due_date, status = ""):

        self.description = description
        self.due_date = due_date
        self.status = status
        self.completion = False
    
    #update_status updates the status of a task
    def update_status(self, current):

        self.status = current

        if self.status.lower() == "complete":
            self.completion = True

        elif self.status.lower() == "incomplete" or self.status.lower() == "PENDING":
            self.completion = False

        else:
            print("Invalid status. Status must be either complete, incomplete, or pending")
    
    def __str__(self):

        if self.completion:
            status = "Complete"
        else:
            status = "Pending"

        return f"{self.description}'s status is {status}, Due Date: {self.due_date}"
    
class List(Tasks):

    def __init__(self, name):
        super().__init__(name, "")
        self.name = name
        self.list = []
    
    #Adds the tasks to the list
    def add_tasks(self, task):
        self.list.append(task)
    
    #Removes the tasks from the list
    def remove_tasks(self, task):

        for task in self.list: #traversing through to the list to find the task that is getting removed

            if task.description == self.description: #if found
                self.list.remove(task)
                print(f"Task is removed from {self.name}'s list of to-dos")
                return
            
        print(f"Task does not exist in {self.name}'s list of to-dos") #if it wasn't found
        return
    
    #display_list traverse through the list of tasks and output each list
    def display_list(self):
        if self.list:

            for i, task in enumerate(self.list, start = 1): #iterating and printing the tasks
                print(f"{i}. {task}")

        else: #if the list is empty
            print(f"There are no stuff to do for {self.name}")
    
    def __str__(self):
        return f"{self.name}'s List of Tasks"
    
class User:

    def __init__(self, name, password = ""):
        self.name = name
        self.password = password
    
    #This function is the password generator
    def generate_password(self, minLen, numbers = True, specialChar = True):
  
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
    
    #login checks if the entered password matches to the saved password
    def login(self, enter_password):
        return enter_password == self.password

    #login_prompt is where the user enter their password to login. This function is kind of janky; it could be better 
    def login_prompt(self):

        print("Welcome, please enter your password")

        while True: #while loop to allow infinite attempts
            input_password = input()

            if self.login(input_password): #if password matches

                print(f"Welcome {self.name}")
                return True
            
            else: #if password does not match or just invalid

                print(f"Invalid Password. Try again.")
                option = input("Please enter q to quit, enter c to create a password, enter any other to try again ")

                if option.lower() == 'q':

                    print("Exit")
                    return False
                
                elif option.lower() == 'c':

                    print("Please create a password")
                    minLen = int(input("Enter the minimum length: "))
                    hasNums = input("Do you want to have numbers? Press y for yes or n for no. ").lower() == "y"
                    hasSpecials = input("Do you want to have special characters? Press y for yes or n for no. ").lower() == "y"
                    user_password = self.generate_password(minLen, hasNums, hasSpecials)
                    print(f"Here is your generated password: {user_password}")
                    return True

if __name__ == "__main__":

    #Testing the code
    user1 = User("Bob", "123")
    user1.login_prompt()

    task1 = Tasks("Task 1", "2022-01-15")
    task2 = Tasks("Task 2", "2023-01-20")
    user_list = List("Work")

    user_list.add_tasks(task1)
    task1.update_status("COMPLETE")
    user_list.add_tasks(task2)

    user_list.display_list()