
height_input = int(input("Triangle height? "))
spacing = height_input - 1
star_unit = 1
counter = 0

while counter < height_input:
    print((' ' * spacing) + ("*" * star_unit))
    star_unit += 2
    spacing -= 1
    counter += 1




# height = int(input("Height of triangle? "))
# count = 0
# status = True

# while status:
#     column = 0
#     star_count = 0
#     while column < (height - 1):
#         print('#', end='')
#         column += 1
#     count += 1 
#     # while star_count < (height + 3):
#     #     print("$", end='')
#     #     star_count += 2
#     print()
#     if count == height:
#         status = False


# height = int(input("Height of your triangle: "))
# height_counter = 0
# counter = 1
# spacing = int(height - counter)
# status = True

# while status:
#     string = "*" * counter
#     print((" " * spacing) + string)
#     counter += 2
#     height_counter += 1
#     if height_counter > height:
#         status = False
