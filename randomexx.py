import random
hello = random.randrange(2,20,2)
print(hello)

import random
while True:
    input("press enter to roll dice...")
    dice = random.randint(1,6)
    print("you rolled the dice..")

    again = input("roll again? yes/no").lower()
    if again != "yes":
        print("game over")
    break
