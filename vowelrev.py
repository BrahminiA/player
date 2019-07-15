n=int(input())
s=input()
b = []

a = "aeiou"
for i in s:
    if i in a:
        continue
    else:
        b.append(i) 
print("".join(b[::-1]))

