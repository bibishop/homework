import random

locations = [random.randint(1, 7) for _ in range(3)]

while True:
    print("Enter the first location and weight:")
    guess1 = int(input())
    weight1 = int(input())
    print("Enter the second location and weight:")
    guess2 = int(input())
    weight2 = int(input())