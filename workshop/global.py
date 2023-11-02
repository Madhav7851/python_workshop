import random 
def guess_number():
    return random.randint(1,100)
target_number=guess_number()
attempts=0
while True:
    user_guess=int(input("guess the number"))
    attempts+=1
    if user_guess==target_number:
        print("Congratulations! You gussed the corect number in",attempts,"attempts")
        break
    elif user_guess<target_number:
        print("Try a heigher number")
    else:
        print("try lower number")