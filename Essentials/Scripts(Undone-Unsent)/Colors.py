"""Colors mixer module"""

col1 = input().lower()
col2 = input().lower()

if (col1 == "red" and col2 == "yellow") or (col1 == "yellow" and col2 == "red"):
    print("Orange")
elif (col1 == "red" and col2 == "blue") or (col1 == "blue" and col2 == "red"):
    print("Violet")
elif (col1 == "yellow" and col2 == "blue") or (col1 == "blue" and col2 == "yellow"):
    print("Green")
elif col1 == col2 == "red":
    print("Red")
elif col1 == col2 == "yellow":
    print("Yellow")
elif col1 == col2 == "blue":
    print("Blue")
else:
    print("Error")
