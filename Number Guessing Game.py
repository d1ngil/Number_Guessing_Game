import random
import time

print("Welcome to the Number Guessing Game!")
time.sleep(1)
print("I'm picking a number between 1 - 100")

answer = random.randint(1, 100)
is_valid = True

while is_valid:
    difficulty = input("Please select a difficulty level (1/2/3): ")
    if difficulty not in ["1", "2", "3"]:
        print("Invalid difficulty, try again!")
    else:
        is_valid = False

def main(difficulty):
    if difficulty == "1":
        chances = 10
        print(f"You have {chances} chances")
    elif difficulty == "2":
        chances = 5
        print(f"You have {chances} chances")
    elif difficulty == "3":
        chances = 3
        print(f"You have {chances} chances")
    else:
        print("Invalid difficulty")

    is_running = True
    attempts = 0

    while is_running and chances > 0:
        try:
            choice = int(input("Pick a number between 1 - 100: "))
            attempts += 1
            if not 0 <= choice <= 101:
                print("I SAID BETWEEN 1 AND 100!")
            elif choice < answer:
                chances -= 1
                print("More!")
            elif choice > answer:
                chances -= 1
                print("Less!")
            elif choice == answer:
                print(f"You win! You guessed the number in {attempts} attempts.")
                is_running = False

            if chances == 0:
                print("You Lost! You used all of your chances!")

        except ValueError:
            print("Invalid value, Try again!")





if __name__ == "__main__":
    main(difficulty)
