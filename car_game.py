print("This is a car game\n")

command = ""
user_input = input("Type start, stop or quit: \n").lower()

status_of_car = "stopped"

while command != "quit":
    print('\n')
    if user_input == "start":
        if status_of_car == "started":
            print("Car is already started")
        else:
            status_of_car = "started"
            print("Car started...Ready to go!")
    elif user_input == "stop":
        if status_of_car == "stopped":
            print("Car is already stopped")
        else:
            status_of_car = "stopped"
            print("Car stopped.")
    elif user_input == "quit":
        break
    else:
        print("I don't understand that...")

    command = user_input
    user_input = input("\nType start, stop or quit: \n").lower()

