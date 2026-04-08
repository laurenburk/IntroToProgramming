item = input("What is your item?\n->")
price = input("How much does this item cost before tax?\n->")
rate = input("What is the tax rate of this item?\n->")

price_float = float(price)
rate_float = float(rate)

amount_tax = price_float * rate_float
total_cost = round(price_float + amount_tax, 2)

def calculate_tax():
    print(item)
    print(" costs ")
    print(price)
    print(" dollars before tax and ")
    print(total_cost)
    print(" after tax.")

calculate_tax()

