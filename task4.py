def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return "ValueError: Use format: <command> <name> <phone number>. "\
                   "Enter 'list' to see all commands and their format."
        except KeyError:
            return f"KeyError: Contact '{args[0][0]}' doesn't exists. To add it use command 'add'. "\
                   "Enter 'list' to see all commands and their format."
        except IndexError:
            return "IndexError: Not enough arguments. "\
                   "Enter 'list' to see all commands and their format."

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return f'Contact "{name}" already exists. To change it use command "change". '\
               "Enter 'list' to see all commands and their format."
    contacts[name] = phone
    return "Contact added."

@input_error 
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."

@input_error 
def show_phone(args, contacts):
    name, = args
    return f'name: {name}, phone: {contacts[name]}'

def show_all(contacts):
    show = ''
    for name, phone in sorted(contacts.items()):
        show += f'name: {name}, phone: {phone}\n'
    return show.strip() if len(show) > 1 else 'No contacts.'

def show_all_comands():
    print('hello - Say Hello')
    print('add - add contact, format: add <name> <phone number>')
    print('change - change contact, format: change <name> <new phone number>')
    print('phone - show contacts phone number, format: phone <name>')
    print('all - show all contacts with phone numbers, format: all')

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "list":
            print(show_all_comands())
        else:
            print("Invalid command. "\
                  "Enter 'list' to see all commands and their format.")

if __name__ == "__main__":
    main()