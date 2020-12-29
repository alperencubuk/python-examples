# Project Euler 22

with open("names.txt","r") as file:
    names = sorted(file.read().split(","))
alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
sum = 0
for name in names:
    nameSum = 0
    for letter in name:
        nameSum += alphabet.get(letter,0)
    nameSum *= names.index(name)+1
    sum += nameSum
print(sum)

# Alperen Cubuk