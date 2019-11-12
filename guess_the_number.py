
import random

should_restart = True
while should_restart:
    print("I am thinking of a number between 1 and 10.")
    my_random_number = random.randint(1, 10)
    counter = 5
    status = True
    while status:
        print(f"You have {counter} guess(es) left.")
        user_num = int(input("What's the number? "))
        if user_num == my_random_number:
            print("Yes! You win!")
            status = False
            should_restart = False
        if user_num < my_random_number:
            print(f"{user_num} is too low.")
            counter -= 1
        if user_num > my_random_number:
            print(f"{user_num} is too high.")
            counter -=1
        if counter == 0:
            print("You ran out of guesses!")
            play_again = input("Do you want to play again? (Y or N) ")
            if play_again == "Y":
                status = False
            else:
                print("Game Over")
                status = False
                should_restart = False
    
        



