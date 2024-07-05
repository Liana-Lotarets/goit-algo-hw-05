# Define the necessary functions.

# Parse the string entered by the user into a command and its arguments.
def parse_input(user_input: str):
    # Arguments may consist of username, phone.
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

# Add exeption to the functions add_contact() and change_contact()
def input_error_add_or_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('Error. Give me a name and a phone please.')
    return inner

# The function adds the contact.
@input_error_add_or_change
def add_contact(args, contacts: dict):
    name, phone = args
    # Check the presence of a contact.
    if contacts.get(name):
        print('Such contact already exists.')
    else:
        contacts[name] = phone
        print(f'Contact added: {name}, phone {phone}')

# The function changes the contact.
@input_error_add_or_change
def change_contact(args, contacts: dict):
    name, phone = args
    # Check the presence of a contact.
    if not contacts.get(name):
        print('No such contact exists.')
    else:
        contacts[name] = phone
        print(f'Contact updated: {name}, phone {phone}')

# Add exeptions to the function show_phone()
def input_error_show_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print('Error. Give me a name please.')
        except KeyError:
            print('Error. No such contact exists.')
    return inner

# The function show a phone number.
@input_error_show_phone
def show_phone(args: list[str], contacts: dict):
    # Single argument "name".
    name = args[0]
    print(contacts[name]) 


def main():
    # Create dictionary of contacts.
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        # Print "Menu".
        print('Please select one of the following commands.\n\
              - Input "Hello" to greet the assistant!\n\
              - Input "add [username] [phone]" to add "username" and their "phone" to the contacts.\n\
              - Input "change [username] [phone]" to change the "phone" of the "username.\n\
              - Input "phone [username]" to print the "phone" of the "username".\n\
              - Input "all" to print all saved contacts.\n\
              - If you want to complete the work with the assistant, then input "close" or "exit".')
        user_input = input('Enter a command: ')
        # Parse the string entered by the user into a command and its arguments.
        command, *args = parse_input(user_input) 

        # React to the command.
        match command:

            # Input "Hello" to greet the assistant!
            case 'hello':
                print('How can I help you?')
            
            # Input "add [username] [phone]" to add "username" and their "phone" to the contacts.
            case 'add':
                add_contact(args,contacts)
            
            # Input "change [username] [phone]" to change the "phone" of the "username.
            case 'change':
                change_contact(args,contacts)

            # Input "phone [username]" to print the "phone" of the "username".
            case 'phone':
                show_phone(args,contacts)
            
            # Input "all" to print all saved contacts.
            case 'all':
                print(contacts)
            
            # If you want to complete the work with the assistant, then input "close" or "exit".
            case 'close' | 'exit':
                print('Good bye!')
                break
            
            # Another case.
            case _:
                print('Invalid command.')

if __name__ == '__main__':
    main()
