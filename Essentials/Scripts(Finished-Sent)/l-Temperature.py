"""Temperature converter"""

Temp = float(input())
from_unit = input()
to_unit = input()
result = None

if from_unit == to_unit:
    result = Temp

if from_unit == "C":
    if to_unit == "K":
        result = Temp + 273.15
    elif to_unit == "F":
        result = (Temp * 9/5) + 32
    elif to_unit == "R":
        result = (Temp + 273.15) * 9/5
if from_unit == "K":
    if to_unit == "C":
        result = Temp - 273.15
    elif to_unit == "F":
        result = (Temp - 273.15) * 9/5 + 32
    elif to_unit == "R":
        result = Temp * 9/5
if from_unit == "F":
    if to_unit == "C":
        result = (Temp - 32) * 5/9
    elif to_unit == "K":
        result = (Temp - 32) * 5/9 + 273.15
    elif to_unit == "R":
        result = Temp + 459.67
if from_unit == "R":
    if to_unit == "C":
        result = (Temp - 491.67) * 5/9
    elif to_unit == "K":
        result = Temp * 5/9
    elif to_unit == "F":
        result = Temp - 459.67

print(f"{result:.2f}")
