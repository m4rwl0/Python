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

            elif choice == "q":
                print("Goodbye, take care")
                break

            else:
                print("Wrong key, please try again")
        except ValueError:
            print("Sorry, I didn't understand that")


if __name__ == "__main__":
    main()
