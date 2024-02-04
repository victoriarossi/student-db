import utils

if __name__ == "__main__":
    print("*********** Welcome to the Student Database ***********")

    utils.printCommands()
    command = input("Input: ")
    while(command.isdigit()):
        command = int(command)
        if(command == 1):
            utils.display_Students(0)
        elif(command == 2):
            utils.display_Courses()
        elif(command == 3):
            utils.display_Prerequisites()
        elif(command == 4):
            utils.create_Student()
        elif(command == 5):
            utils.create_Course()
        elif(command == 6):
            utils.create_Prerequisites()
        else:
            print("Invalid command, please try again.")
            utils.printCommands()

        command = input("Input: ")