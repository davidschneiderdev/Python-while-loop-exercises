
width = int(input("Width? "))
height = int(input("Height? "))

height_count = 1

while height_count < height:
    if height_count == 1:
        print(("*") * width)
    if height_count == (height-1):
        print(("*") * width)
    elif height_count != height:
        print("*" + (" " * (width-2)) + ("*"))
    height_count += 1



    