welcome_prompt = "Welcome, what would you like to do today?\nTo list all patients, press 1\nTo run diagnosis, press 2\nTo quit, press q"
questions = [
    "1. Do you usually have a bottle of water with you when you are outside? y/n",
    "2. Do you drink bottled water at home? y/n",
    "3. Do you frequently consume bottled water? y/n",
    "4. Do you consume any fluid before you feel thirsty? y/n",
    "5. Do you feel full after drinking liquids? y/n",
    "6. Do you know what the recommended daily amount of water is for a healthy adult? y/n",
    "7. Do you drink at least 2 liters of water per day? y/n",
    "8. How many cups of fluid are recommended per day\n: a) 8-10, b) 6-8, c) 4-6?",
    "9. Do you have any disease or health problems? y/n",
]

correct_answers = ["y", "y", "y", "y", "y", "y", "y", "a", "n"]
user_answers = []


def main():
    while True:
        print(welcome_prompt)
        choice = input()

        if choice == "1":
            print("You have chosen to list all patients")
            try:
                with open("medical_records.txt", "r") as file:
                    content = file.read()
                    print(content)
            except FileNotFoundError:
                print("File not found. No medical records available.")

        elif choice == "2":
            print("Running the diagnosis")
            name = input("What is your name?")

            score = 0
            with open("medical_records.txt", "a") as file:
                file.write(name + "\n" + "\n")

                for x in range(len(questions)):
                    print(questions[x])
                    file.write(questions[x] + "\n")

                    answer = input("")
                    user_answers.append(answer)
                    file.write(user_answers[x] + "\n")

                    if user_answers[x] == correct_answers[x]:
                        perfect = "Perfect"
                        print(perfect)
                        file.write(perfect + "\n")
                        score += 1
                    else:
                        wrong = "Wrong answer"
                        print(wrong)
                        file.write(wrong + "\n")

                if score > 6:
                    hydrated = "You are hydrated, but keep going."
                    print(hydrated)
                    file.write(hydrated + "\n" + "\n")
                    break
                elif score >= 3:
                    some_hydrated = (
                        "You have some hydration, but you need to take care of it more."
                    )
                    print(some_hydrated)
                    file.write(some_hydrated + "\n" + "\n")
                    break
                else:
                    low_hydrated = "You have low hydration; you need to drink more."
                    print(low_hydrated)
                    file.write(low_hydrated + "\n" + "\n")
                    break

        elif choice == "q":
            print("Goodbye, take care")
            break  # Exit the loop when the user chooses to quit

        else:
            print("Wrong key, please try again")


if __name__ == "__main__":
    main()
