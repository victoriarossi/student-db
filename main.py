import utils

if __name__ == "__main__":
    print("*********** Welcome to the Student Database ***********")

    utils.printCommands()
    command = input("Input: ")
    while(utils.checkCommand(command)):
        if(command.isalpha()):
            utils.printCommands()
            command = input("Input: ")
            continue
        else:
            command = int(command)
        if(command == 1):
            utils.print_Display_Commands()
            command = input("Input: ")
            if(command.isalpha() and command.upper() == 'B'):
                utils.printCommands()
                command = input("Input: ")
                continue
            elif(command.isalpha() and command.upper() == 'h'):
                utils.print_Display_Commands()
                command = input("Input: ")
                continue
            elif(command.isdigit()):
                command = int(command)
                if(command == 1): 
                    utils.display_Students()
                elif(command == 2):
                    utils.display_Courses()
                elif(command == 3):
                    utils.display_Prerequisites()
                if(command == 4): 
                    utils.get_student()
                elif(command == 5):
                    utils.get_course()
                elif(command == 6):
                    utils.get_prerequisites()
                elif(command == 7):
                    utils.get_registrations()
        elif(command == 2):
            utils.print_Update_Commands()
            command = input("Input: ")
            if(command.isalpha() and command.upper() == 'B'):
                utils.printCommands()
                command = input("Input: ")
                continue
            elif(command.isalpha() and command.upper() == 'h'):
                utils.print_Update_Commands()
                command = input("Input: ")
                continue
            elif(command.isdigit()):
                command = int(command)
                if(command == 1):
                    utils.create_Student()
                elif(command == 2):
                    utils.create_Course()
                elif(command == 3):
                    utils.create_Prerequisites()
                elif(command == 4):
                    utils.create_Registration()
                elif(command == 5):
                    utils.update_student()
                elif(command == 6):
                    utils.update_course()
                elif(command == 7):
                    utils.update_registration()
        else:
            print("Invalid command, please try again.")
            utils.printCommands()

        command = input("Input: ")