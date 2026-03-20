# Safe Keyboard Input Logger (Educational Purpose Only)

def main():
    print("This program logs input WITH USER CONSENT.")
    print("Type 'exit' to stop.\n")

    with open("input_log.txt", "a") as file:
        while True:
            user_input = input("Enter text: ")

            if user_input.lower() == "exit":
                print("Exiting logger.")
                break

            file.write(user_input + "\n")


if __name__ == "__main__":
    main()
