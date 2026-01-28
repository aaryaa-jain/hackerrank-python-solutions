# Problem: sWAP cASE
# Platform: HackerRank

s = input()
result = ""

for ch in s:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print(result)
