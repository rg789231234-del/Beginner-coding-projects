#hey guys, hope you are all doing well
#today, i will show you how to make a simple countdown timer program in Python
#let's get started
#first, we need to import time
import time

second=int(input("Enter second for countdown:"))#user input
print("Countdown starting...")
time.sleep(1) #interval

while second>-1: #after the countdown gets to 0, the program completely stops
    print(second)
    time.sleep(1) #this is for the interval between numbers
    second=second-1 #used for counting down

print("Countdown finished")
