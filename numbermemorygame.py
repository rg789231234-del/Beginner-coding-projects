import random #for random number generation
import time#for waiting time

print("Welcome to the number memory game")
number=random.randint(1000,9999)#random number genration
print("Remember this number:", number)
time.sleep(2)#interval
print("\n"*50)#used to clear spaces in the screen

print("Interval...")
time.sleep(10)
guess=input("Enter the number you saw")
if guess==str(number):
    print("Correct")
else:
    print("Wrong")
