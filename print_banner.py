
user_prompt = input("Text? ")
user_len = len(user_prompt)
box_len = user_len + 4

print("*" * box_len)
print("* " + user_prompt + " *")
print("*" * box_len)

