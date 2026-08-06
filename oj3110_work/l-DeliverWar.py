"""delivery cost or something"""

Term, Dest = input().split()
Weight = float(input())
Totalize = 0

if (Term == "BKK" and Dest == "CNX"):
    Totalize = (Weight * 30) + 10
elif (Term == "CNX" and Dest == "UBP"):
    Totalize = (Weight * 40) + 15
elif (Term == "UBP" and Dest == "BKK"):
    Totalize = (Weight * 40) + 20
elif (Term == "BKK" and Dest == "PKT"):
    Totalize = (Weight * 50) + 25
elif (Term == "PKT" and Dest == "CNX"):
    Totalize = (Weight * 60) + 30
elif (Term == "UBP" and Dest == "PKT"):
    Totalize = (Weight * 70) + 40
else:
    Totalize = "Error"

if Totalize == "Error":
    print(Totalize)
elif Totalize:
    print(f"{Totalize:.2f}")
