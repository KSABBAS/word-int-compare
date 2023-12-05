dic={
    "a":1,
    "A":1,
    "b":3,
    "B":3,
    "c":3,
    "C":3,
    "d":2,
    "D":2,
    "e":1,
    "E":1,
    "f":4,
    "F":4,
    "g":2,
    "G":2,
    "h":4,
    "H":4,
    "i":1,
    "I":1,
    "j":8,
    "J":8,
    "k":5,
    "K":5,
    "l":1,
    "L":1,
    "m":3,
    "M":3,
    "n":1,
    "N":1,
    "o":1,
    "O":1,
    "p":3,
    "P":3,
    "q":10,
    "Q":10,
    "r":1,
    "R":1,
    "s":1,
    "S":1,
    "T":1,
    "t":1,
    "U":1,
    "u":1,
    "v":4,
    "V":4,
    "w":4,
    "W":4,
    "X":8,
    "x":8,
    "y":4,
    "Y":4,
    "z":10,
    "Z":10,
}
word=input("enter the word1 : ")
word2=input("enter the word2 : ")
list(word)
sum=0
sum1=0
for i in word:
    sum+=dic[i]
for i in word2:
    sum1+=dic[i]
if (sum1==sum):
    print("even")
elif max(sum1,sum)==sum1:
    print("player 2")
elif max(sum1,sum)==sum:
    print("player 1")