"""what"""

stat = input()
stuff = int(input())
things = []
totalize = 0

for _ in range(stuff):
    things.append(float(input()))

if stat == "Y":
    totalize = sum(things) - (sum(things) * 0.05)
elif stat == "N" and sum(things) >= 500:
    totalize = sum(things) - (sum(things) * 0.03)
else:
    totalize = sum(things)

if str(f"{totalize:.3f}")[-1] >= "5":
    totalize += 0.005

print(f"{totalize:.2f}")
