import sys
# Write your code here
# num_coffee = int(input())

# print(f"For {num_coffe} cups of cofee you will need:")
# print(f"{200 * num_coffe} ml of water")
# print(f"{50 * num_coffe} ml of milk")
# print(f"{15 * num_coffe} g of coffee beans")

water_input_cnt = 400
milk_input_cnt = 540
coffee_input_cnt = 120
cup_input = 9
coffee_machine_money = 550


def fill_coffee_machine():
    different = 0

    print("Write how many ml of water o you want to add:")
    global water_input_cnt
    water_input_cnt = int(input()) + water_input_cnt
    print("Write how many ml of milk do you want to add:")
    global milk_input_cnt
    milk_input_cnt = int(input()) + milk_input_cnt
    print("Write how many grams of coffee do you want to add:")
    global coffee_input_cnt
    coffee_input_cnt = int(input()) + coffee_input_cnt
    print("Write how many disposable cups of coffee do you want to add:")
    global cup_input
    cup_input = int(input()) + cup_input
    # coffee_machine_inf()

    # if water_input != 0 and milk_input != 0 and coffee_input != 0 and cup_input != 0:
    #     water_input_cnt = water_input // 200
    #     milk_input_cnt = milk_input // 50
    #     coffee_input_cnt = coffee_input // 15
    #     coffee_machine = 0
    #
    #     if water_input_cnt <= milk_input_cnt and water_input_cnt <= coffee_input_cnt:
    #         coffee_machine = water_input_cnt
    #     elif milk_input_cnt <= water_input_cnt and milk_input_cnt <= coffee_input_cnt:
    #         coffee_machine = milk_input_cnt
    #     elif coffee_input_cnt <= milk_input_cnt and coffee_input_cnt <= water_input_cnt:
    #         coffee_machine = coffee_input_cnt
    #     # coffee_machine = water_input + milk_input + coffee_input
    #     one_cup_ingredients = 200 + 50 + 15
    #     # level_one = coffee_machine // one_cup_ingredients
    #     different = coffee_machine - cup_input
    #     if different > cup_input:
    #         print(f"Yes, I can make that amount of coffee (and even {different} more than that)")
    #     elif different == 0:
    #         print('Yes, I can make that amount of coffee')
    #     elif coffee_machine < cup_input:
    #         print(f'No, I can make only {coffee_machine} cup(s) of coffee')
    #     elif cup_input < coffee_machine:
    #         print(f'No, I can make only {coffee_machine} cup(s) of coffeeYes, I can make that amount of coffee (and even {different} more than that)')
    # elif water_input == 0 and milk_input == 0 and coffee_input == 0 and cup_input > 0:
    #     print('No, I can make only 0 cups of coffee')
    # elif water_input == 0 and milk_input == 0 and coffee_input == 0 and cup_input == 0:
    #     print('Yes, I can make that amount of coffee')
    # elif water_input != 0 and milk_input != 0 and coffee_input != 0 and cup_input == 0:
    #     print('Yes, I can make that amount of coffee (and even 1 more than that)')


def buy_coffee_machine():
    global coffee_input_cnt
    global water_input_cnt
    global milk_input_cnt
    global cup_input
    global coffee_machine_money

    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee_type = input()
    if coffee_type == "1":
        if water_input_cnt < 250:
            print("Sorry, not enough water!")
        else:
            coffee_input_cnt = coffee_input_cnt - 16
            water_input_cnt = water_input_cnt - 250
            coffee_machine_money = coffee_machine_money + 4
            cup_input = cup_input - 1
            print("I have enough resources, making you a coffee!")
    elif coffee_type == "2":
        if water_input_cnt < 350: # or coffee_input_cnt <20 or milk_input_cnt < 75:
            print("Sorry, not enough water!")
        else:
            water_input_cnt = water_input_cnt - 350
            milk_input_cnt = milk_input_cnt - 75
            coffee_input_cnt = coffee_input_cnt - 20
            coffee_machine_money = coffee_machine_money + 7
            cup_input = cup_input - 1
            print("I have enough resources, making you a coffee!")
    elif coffee_type == "3":
        if water_input_cnt < 200 or milk_input_cnt < 100 or coffee_input_cnt < 12:
            print("Sorry, not enough water!")
        else:
            water_input_cnt = water_input_cnt - 200
            milk_input_cnt = milk_input_cnt - 100
            coffee_input_cnt = coffee_input_cnt - 12
            coffee_machine_money = coffee_machine_money + 6
            cup_input = cup_input - 1
            print("I have enough resources, making you a coffee!")
    elif coffee_type == "exit":
        sys.exit()
    # coffee_machine_inf()


def take_coffee_machine():
    global coffee_machine_money
    print(f"I gave you ${coffee_machine_money}")
    coffee_machine_money = 0
    # coffee_machine_inf()


def coffee_machine_inf():
    global coffee_input_cnt
    global water_input_cnt
    global milk_input_cnt
    global cup_input
    global coffee_machine_money

    print("The coffee machine has:")
    print(f"{water_input_cnt} of water")
    print(f"{milk_input_cnt} of milk")
    print(f"{coffee_input_cnt} of coffee beans")
    print(f"{cup_input} of disposable cups")
    print(f"{coffee_machine_money} of money")


def start_coffee_machine_action():
    # stack = [buy_coffee_machine()]
    while True:
        print("write action(buy, fill, take, remaining, exit):")
        customer_input = input()
        if customer_input == "buy":
            # stack.append(buy_coffee_machine())
            buy_coffee_machine()
        elif customer_input == "fill":
            # stack.append(fill_coffee_machine())
            fill_coffee_machine()
        elif customer_input == "take":
            # stack.append(take_coffee_machine())
            take_coffee_machine()
        elif customer_input == "remaining":
            coffee_machine_inf()
        elif customer_input == "back":
            # stack.peek()
            buy_coffee_machine()
        elif customer_input == "exit":
            break


# coffee_machine_inf()
start_coffee_machine_action()

