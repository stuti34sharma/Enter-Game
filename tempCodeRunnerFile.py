import time 
import random 


# a list to save the reaction time 
reaction_time = []

#have a loop that goes for 5 times and then give total score

#to have a message saying "get ready" - then wait random seconds and wait for enter

for i in range(5):
    print(f"Round {i+1}")

    if i != 0: #range fn starts from 0 by default -> this skips the go again message in the first iteration
        print("Go again!")
    print("Get ready to press Enter when trigger comes!")
    seconds = random.uniform(2,6) #how much time it ll take to give the promt to press enter
    time.sleep(seconds) # and for that amount of time the program will be stopped
    start = time.time() # to start recording 
    input("Press Enter NOW!")
    end = time.time() # and record after which second did the user press enter
    #wait random seconds and give trigger in some form for user to click space bar 
    react_time = end - start
    
    #recorded time to be added into list
    reaction_time.append(react_time)


print(f"Quickest reaction time : {min(reaction_time):.3f} seconds") # .3f formats to 3 decimal places for readability 
print(f"Slowest reaction time : {max(reaction_time):.3f} seconds")
print(f"Average reaction time : {sum(reaction_time)/len(reaction_time)} seconds")

