price_list = []
user_input = ''

def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list

def average_price(prices_list):
    return(sum(prices_list)/len(prices_list))

def get_max_price(prices_list):
    return(max(prices_list))

def menu():
    print("1 > Add price")
    print("2 > Show average price")
    print("3 > Show highest price")
    print("q > Quit")
    print("-------------------------------")
    user_input = input("Enter your input:")
    # print(type(user_input))

    while(user_input != 'q'):
        if user_input == '1':
            new_price = int(input("Enter the price you want to add: "))
            print("Price list after addition:", add_price(price_list, new_price))
        elif user_input == '2':
            print("Average price: ", average_price(price_list))
        elif user_input == '3':
            print("Highest price: ", get_max_price(price_list))
        else:
            print("Invalid input, please try again.")
        print("1 > Add price")
        print("2 > Show average price")
        print("3 > Show highest price")
        print("q > Quit")
        print("-------------------------------")
        user_input = input("Enter your input:")

def get_price():
    priceListLength = input("Enter the number items: ")
    for iterable in range(int(priceListLength)):
        price_list.append(int(input(f"Enter Item {iterable} price: ")))
    print("Thank you!")

get_price()
menu()

print("Thank you have a great day!")