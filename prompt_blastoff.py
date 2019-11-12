

start = True
while start:
    user_counter = int(input("Enter number to start countdown: "))
    if user_counter > 20:
        print("Please do not enter a number larger than 20.")
    else:
        status = True
        while status:
            print(user_counter)
            user_counter -= 1
            if user_counter == 0:
                print(user_counter)
                status = False
                start = False
                
                    

