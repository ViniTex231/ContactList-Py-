names_list = []
numbers_list = []


def addContact():
    name = input("Type the name: ")
    names_list.append(name)
    number = int(input("Type the number: "))
    numbers_list.append(number)
    print("Successfully!")


def removeContact():
    name = input("Type the name: ")
    names_list.remove(name)
    number = int(input("Type the number: "))
    numbers_list.remove(number)
    print("Successfully!")


def searchContact():
    name = input("Type the name: ")
    if name in names_list:
        position = names_list.index(name)
        print(f"The number is {numbers_list[position]}")
    else:
        print("This name not in contact list")


def showContact():
    print(names_list)
    print(numbers_list)


while True:
    print("Welcome to the Virtual Contact List!")
    print("1 - Add a new contact")
    print("2 - Remove a contact")
    print("3 - Search a contact")
    print("4 - Show the contact list")
    print("5 - Exit")

    option = int(input("Type the option: "))
    if option == 1:
        addContact()
    elif option == 2:
        removeContact()
    elif option == 3:
        searchContact()
    elif option == 4:
        showContact()
    elif option == 5:
        break
    else:
        print("Incorrect option")



