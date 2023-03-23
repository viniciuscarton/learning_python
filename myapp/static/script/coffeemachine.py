MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = []
coins = {
    "q": 0.25,
    "d": 0.10,
    "n": 0.05,
    "p": 0.01
}
totaltopay = 0


def setorder(order):
    new_order = MENU[f"{order}"]
    new_order_i = new_order["ingredients"]
    global new_order_c
    new_order_c = new_order["cost"]
    money.append(new_order_c)
    for i in new_order_i:
        if resources[f"{i}"] > new_order_i[f"{i}"]:
            resources[i] -= new_order_i[i]
            global g_resources
            g_resources = resources
        else:
            missing = resources[i] - new_order_i[i]
            print(f"Sorry, not enough {i} ({missing})")
            quit()


def currentr():
    print("$" + str(sum(money)))


def neworder():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    setorder(order)
    q = float(input("Insert quarters: "))
    d = float(input("Insert dimes: "))
    n = float(input("Insert nickels: "))
    p = float(input("Insert pennies: "))
    totalpaying = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    if float(totalpaying) >= new_order_c:
        change = round(totalpaying - new_order_c, 2)
        print(f"Thanks. Enjoy it! And here is your change: ${change}")
    else:
        print("That's not enough.")


def menu():
    print("Hello! What would you like to do?")
    print("1 for new order")
    print("2 for current machine $")
    print("3 for current machine resources")


menu()
option = int(input("Enter your number: "))
while option >= 1 <= 3:
    if option == 1:
        neworder()
    elif option == 2:
        currentr()
    elif option == 3:
        print(g_resources)
    else:
        print("Thanks for using me :D")
        quit()

    print()
    menu()
    option = int(input("Enter your number: "))
