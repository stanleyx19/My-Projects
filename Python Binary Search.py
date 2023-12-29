import time
import random

#Regular Search Algorithm
def regular_search(list, target):

    #Traversing the list linearly
    for i in range(len(list)):
        if list[i] == target: #if found
            return i
        
    return -1

#Binary Search Algorithm 
def binary_search(list, goal, low = None, high = None):

    if low == None: #Makes the low 0 if low was not given in the parameter
        low = 0

    if high == None: #Makes the high the length of the list -1 if high was not given in the parameter
        high = len(list) - 1

    if high < low: #Catching a potential error
        return -1
    
    midpoint = (low + high)//2 #Midpoint of the list

    #Actual Binary Search occurs via recursion 
    if list[midpoint] == goal: #if we found the element we are searching for
        return midpoint
    
    elif list[midpoint] < goal: #if the midpoint is smaller than the element we are searching for
        return binary_search(list, goal, midpoint+1, high)
    
    else: #if the midpoint is larger than the element we are searching for 
        return binary_search(list, goal, low, midpoint-1)


if __name__ == "__main__":
    
    #Checks long does each search takes
    #Time Complexity of regular_search is O(n) due to the fact we are traversing each element of a list (contains n elements)
    #Time Complexity of binary_search is O(log n) due to the fact we are splitting the list in half during each search

    length = 10000

    sorted_set = set()
    while len(sorted_set) < length:
        sorted_set.add(random.randint(-2*length, 2*length))
    sorted_list = sorted(list(sorted_set))

    start = time.time()
    for element in sorted_list:
        regular_search(sorted_list, element)
    end = time.time()
    print("Regular Search: ", (end - start)/length, "seconds")

    start = time.time()
    for element in sorted_list:
        binary_search(sorted_list, element)
    end = time.time()
    print("Binary Search: ", (end - start)/length, "seconds")

    #The commented section below is testing if the searching algorithms works

    """
    user_list = []
    user_n_amount = int(input("Enter a number of elements in the list: "))

    for j in range(user_n_amount):
        number = int(input("Enter a number: "))
        user_list.append(number)

    target_number = int(input("Enter a target number: "))
    print(f'Regular Search: Target is found at {regular_search(user_list, target_number)}')
    print(f'Binary Search: Target is found at {binary_search(user_list, target_number)}')
    """""
    