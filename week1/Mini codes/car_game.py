# Car game 
print("Car mini game")
state = "not"
while True:
    command = input("> ").lower()
    if command == "help":
        print("""
Start - to start the car 
Stop - to stop the car
Quit - to quit
            """)
    elif command == "quit":
        print("Good bye")
        break
    elif command == "start":
        if state == "not":
            state = "started"
            print("Car started")
        else:
            print("car already started")
    elif command == "stop":
        if state == "started":
            state = "not"
            print("Car stopped")
        else:
            print("Start the car ")
    else:
        print("Command not understood use help")