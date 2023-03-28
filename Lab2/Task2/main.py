import my_container


if __name__ == "__main__":

    username = input("Enter username: ")
    container = my_container.MyContainer(username)
    is_executing = True

    while is_executing:
        command_list = '''
            add <key> [key, …]
            remove <key>
            find <key> [key, …]
            list
            grep <regex>
            save
            load
            switch
            exit
            '''
        print(command_list)
        command = input("Enter command: ")

        match command:
            case "add":
                key = input("Input key to add: ")
                key = key.split()
                for el in key:
                    container.add(el)

            case "remove":
                key = input("Input key to remove: ")
                container.remove(key)
            case "find":
                key = input("Input key to find: ")
                key = key.split()
                for el in key:
                    container.find(el)
            case "list":
                container.list()
            case "grep":
                key = input("Input regex to match: ")
                container.grep(key)
            case "save":
                container.save()
            case "load":
                container.load()
            case "switch":
                answer = input("Do you want save your container?(y/n): ")
                if answer.lower() == 'y':
                    container.save()
                user = input("Enter username to switch: ")
                container.switch(user)
            case "exit":
                answer = input("Do you want save your container?(y/n): ")
                if answer.lower() == 'y':
                    container.save()
                is_executing = False
            case _:
                print("There is no such command")
