
import random

def multiplications():
    for i in range(10):
        randomNumber = random.randint(0, 10)
        randomNumber1 = random.randint(0, 10)

        answer = -1
        while int(answer) != randomNumber * randomNumber1:
            print()
            answer = input(f" {randomNumber} x {randomNumber1} = ")
            if int(answer) == randomNumber * randomNumber1:
                print("✅")
            else:
                print("❌")


                