 def display_multiplication_table(num):
    for i in range(1, 13):
        print(f"{num} * {i} = {num * i}")

def main():
    run_program = "yes"

    while run_program.lower() == "yes":
        try:
            number = int(input("Enter an integer: "))
            if number >= 0:
                display_multiplication_table(number)
            else:
                print("This program does not handle negative number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

        run_program = input("Would you like to run the program again? ")
        if run_program.lower() != "yes":
            print("Exiting Program...")

main()
