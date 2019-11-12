
counter = 10

status = True
while status:
    print(counter)
    counter -= 1
    if counter == 0:
        print(counter)
        print("You have arrived!")
        status = False

        