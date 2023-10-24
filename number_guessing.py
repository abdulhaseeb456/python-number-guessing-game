import random

def play():
    print("\n-----------------------------")
    random_number = random.randint(1, 10)
    attempts = 0
    numbers = {
        1: "1st",
        2: "2nd",
        3: "3rd",
        4: "4th",
        5: "5th"
    }

    while True:
        if attempts < 5:
            try:
                user_input = int(input("<< Enter a number between 1 & 10: "))
                if user_input >= 1 and user_input <= 10:
                    attempts += 1
                    if user_input == random_number:
                        print(f">> Hey, you won in {numbers.get(attempts)} attempt; You: {user_input}, Computer: {random_number}, Attempts: {5 - attempts}")
                        if input(">< Press any key to exit or 'y' to play again: ") == "y":
                            attempts = 0
                            play()
                        else:
                            break
                    elif user_input < random_number:
                        print(f"<? Try a Higher one than {user_input} - <Attempts: {5 - attempts}>")
                    elif user_input > random_number:
                        print(f"<? Try a Lower one than {user_input} - <Attempts: {5 - attempts}>")
                else:
                    print("<? Not in the given range(1-10)")

            except ValueError:
                print("<? Invalid Value")
        else:
            print(f">< Failed: You Tried All Attempts {attempts}/5")
            if input(">< Press any key to exit or 'y' to play again: ") == "y":
                attempts = 0
                play()
            else:
                break

    print("-----------------------------")
    exit()
    
if __name__ == "__main__":
    play()
