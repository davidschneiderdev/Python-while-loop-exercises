
counter = 10

status = True
while status:
    print(counter)
    counter -= 1
    if counter == 0:
        print(counter)
        status = False

