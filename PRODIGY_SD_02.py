import random

print("Player 1, enter the following details: ")
start = int(input("What should be the starting range of the numbers? -->"))
endit = int(input("What should be the ending range of the numbers? -->"))
if (start >= endit):
	print("The ending number is either same or smaller than the beginning number which is not allowed")
	exit(0)
print(f"The number is between {start} and {endit}")
guess = random.randint(start,endit)
count = 1
your = int(input(f"Enter Guess No.{count}:"))
while(guess != your):
    if guess > your:
        print("Your guess is too low")
        count+=1
        
    elif guess < your:
        print("Your guess is too high")
        count+=1
        
    your = int(input(f"Enter Guess No.{count}:"))
print(f"The number was successfully guessed in {count} attempts")
