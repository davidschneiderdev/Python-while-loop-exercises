
counter = 0

wants_coin = True

while wants_coin:
    print(f"You have {counter} coins.")
    question = input("Do you want another (yes or no)? ")
    if question == "yes":
        counter += 1
    else:
        break

print("Bye")


