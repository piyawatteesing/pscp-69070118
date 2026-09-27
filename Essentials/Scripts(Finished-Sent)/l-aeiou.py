"""tungtungaeiou"""

word = input().lower()
a = 0
e = 0
i = 0
o = 0
u = 0

for step in range(len(word)):
    if word[step] == "a":
        a += 1
    elif word[step] == "e":
        e += 1
    elif word[step] == "i":
        i += 1
    elif word[step] == "o":
        o += 1
    elif word[step] == "u":
        u += 1

if a:
    print("a :", a)
if e:
    print("e :", e)
if i:
    print("i :", i)
if o:
    print("o :", o)
if u:
    print("u :", u)
