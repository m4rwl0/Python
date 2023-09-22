welcome_prompt = "Welcome, what would you like to do today?\nTo list all patients, press 1\nTo run diagnosis, press 2\nTo quit, press"


def main():
    while True:
        try:
            print(welcome_prompt)
            choice = input("")

            if choice == "1":
                print("You have chosen to list all patients")

            elif choice == "2":
                print("Running the diagnosis")
                question_1 = input(
                    "Do you usually have a bottle of water	with you when you are outside? y/n"
                )
                question_2 = input("Do you drink bottled water at home? y/n")
                question_3 = input("Do you frequently consume	bottled	water? y/n")
                question_4 = input(
                    "Do you consume any fluid before you feel thirsty? y/n"
                )
                question_5 = input("Do you feel full after drinking liquids? y/n")
                question_6 = input(
                    "Do you know what the recommended daily amount of water is for a healthy adult? y/n"
                )
                question_7 = input(
                    "Do you drink at least 2 liters of water per day? y/n"
                )

            elif choice == "q":
                print("Goodbye, take care")
                break

            else:
                print("Wrong key, please try again")
        except ValueError:
            print("Sorry, I didn't understand that")


if __name__ == "__main__":
    main()
