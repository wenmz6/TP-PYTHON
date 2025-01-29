import random

lost = False
score = 0

while not lost:
    number = random.randrange(0, 16)
    bin_number = bin(number)
    guess = input("Quel est la valeur décimale de " + bin_number + " ? \n")

    if guess == str(number):
        print("Bravo")
        score += 1
    else:
        print("Tu as perdu: c'était ", number)
        lost = True

print("Score : ", score)
