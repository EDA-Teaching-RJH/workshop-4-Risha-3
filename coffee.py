def payment(money):
     counter = 1
     while counter == 1:
          user_pay = ("Please insert cash only, and only 50p 20p 10p 5p: ")



coffee_types = [['espresso', 2.00],
                ['latte', 1.50],
                ['frappe', 1.70],
                ['mocha', 1.15],
                ['cappuccino', 1.20]]
print("\nMenu:",
      "\n *Espresso - 2.00",
      "\n *Latte - 1.50",
      "\n *Frappe - 1.70",
      "\n *Mocha - 1.15"
      "\n *Cappuccino - 1.20 ",)

coffee_option = input("\nSelect option: ").lower()


for coffee in coffee_types:
        if coffee[0] == coffee_option:
            cost = coffee[1]
            print(f"This is available, please pay: £{cost:.2f}")
            payment()
        else:
            print("This is unavailable, please try again")







