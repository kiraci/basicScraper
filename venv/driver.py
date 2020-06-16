from currencyConverter import Currency
from newsGatherer import News

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

print("Welcome To The Currency Program of the OBA\n")

news = News()

flag = True

currency = Currency()

while flag:

    printMenu()

    option = input("\nPlease Select an Option to Convert to TRY: ")

    if option == '1':
        print("\nUSD/TRY = " + currency.printValue('1'))
        news.googleNews("Dolar")
    elif option == '2':
        print("\nEUR/TRY = " + currency.printValue('2'))
        news.googleNews("Euro")
    elif option == '3':
        print("\nGBP/TRY = " + currency.printValue('3'))
        news.googleNews("Ingiltere Sterlini")
    elif option == '4':
        print("\nGram Altın = " + currency.printValue('4'))
        news.googleNews("Gram Altın")
    elif option == '5':
        print("\nYarım Altın = " + currency.printValue('5'))
        news.googleNews("Yarım Altın")
    elif option == '6':
        print("\nCAD/TRY = " + currency.printValue('6'))
        news.googleNews("Kanada Doları")
    elif option == '0':
        flag = False
    else:
        print("\nPlease Give an Valid Option\n")

print("\nSee You Later...")
