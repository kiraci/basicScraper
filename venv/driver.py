import currencyConverter
import newsGatherer

def printMenu():
    print("""
        1- USD\n
        2- EUR\n
        3- GBP\n
        4- Gram Altın\n
        5- Yarım Altın\n
        6- CAD\n
        0- EXIT
        """)


print("Welcome To The Program\n")

flag = True

while flag :

    printMenu()

    option = input("\nPlease Select an Option to Convert to TRY: ")


    if option == '1' :
        print("")
    elif option == '2':
        print("")
    elif option == '3':
        print("")
    elif option == '4':
        print("")
    elif option == '5':
        print("")
    elif option == '6':
        print("")
    elif option == '0':
        flag = False
    else:
        print("\nPlease Give an Valid Option\n")

print("\nSee You Later...")

