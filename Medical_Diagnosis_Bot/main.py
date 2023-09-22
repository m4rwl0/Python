welcome_prompt = "Welcome, what would you like to do today?\nTo list all patients, press 1\nTo run diagnosis, press 2\nTo quit, press"
questions = [
    "1. Do you usually have a bottle of water	with you when you are outside? y/n",
    "2. Do you drink bottled water at home? y/n",
    "3. Do you frequently consume	bottled	water? y/n",
    "4. Do you consume any fluid before you feel thirsty? y/n",
    "5. Do you feel full after drinking liquids? y/n",
    "6. Do you know what the recommended daily amount of water is for a healthy adult? y/n",
    "7. Do you drink at least 2 liters of water per day? y/n",
    "8. How many cups of fluid are recommended per day \n: a) 8-10, b) 6-8, c) 4-6?",
    "9. Do yo have any disease or health problems? y/n",
]

correct_anwsers = ["y", "y", "y", "y", "y", "y", "y", "a", "n"]
user_anwsers = []


def main():
    # while True:
    # try:
    print(welcome_prompt)
    choice = input("")

    if choice == "1":
        print("You have chosen to list all patients")

    elif choice == "2":
        print("Running the diagnosis")

        score = 0
        for x in range(len(questions)):
            print(questions[x])
            anwser = input("")
            user_anwsers.append(anwser)
            print(user_anwsers)
            if user_anwsers[x] == correct_anwsers[x]:
                print("Perfect")
                score += 1
            else:
                print("Wrong anwser")

        print(score)

        if score > 6:
            print("You are hydrated, but keep going.")
        elif score >= 3:
            print("You have some hydration, but you need to take care about it more.")
        else:
            print("You have no hydration, you need to drink.")

    elif choice == "q":
        print("Goodbye, take care")
        # break

    # else:
    #     print("Wrong key, please try again")


# except ValueError:
# print("Sorry, I didn't understand that")


if __name__ == "__main__":
    main()
