import random

locations = [random.randint(1, 7) for _ in range(3)]

while True:
    print("Enter the first location and weight:")
    guess1 = int(input())
    weight1 = int(input())
    print("Enter the second location and weight:")
    guess2 = int(input())
    weight2 = int(input())
    print("Enter the third location and weight:")
    guess3 = int(input())
    weight3 = int(input())
    if guess1 != guess2 and guess1 != guess3 and guess2 != guess3:
