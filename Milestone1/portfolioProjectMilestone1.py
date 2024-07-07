class ItemToPurchase:

    #Constructor with initial values and defines types
    def __init__(self, item_name="none", item_price=float(0), item_quantity=int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #Function to format and print the items cost and return the items total
    def print_item_cost(self):
        item_total = round(self.item_price * self.item_quantity, 2)
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, item_total))
        return item_total


def main ():
    item1_name = input("Enter the item name: ")
    item1_cost = float(input("Enter the item price: "))
    item1_quantity = int(input("Enter the item quantity: "))
    #pass item1 to ItemToPurchase class
    item1 = ItemToPurchase(item1_name, item1_cost, item1_quantity)
    item2_name = input("Enter the item name: ")
    item2_cost = float(input("Enter the item price: "))
    item2_quantity = int(input("Enter the item quantity: "))
    #pass item2 to ItemToPurchase class
    item2 = ItemToPurchase(item2_name, item2_cost, item2_quantity)
    print("TOTAL COST")
    #Variable to ItemToPurchase.print_item_cost() for both items and add the result
    total = (ItemToPurchase.print_item_cost(item1) + ItemToPurchase.print_item_cost(item2))
    print("Total: ${}".format(total))


if __name__ == '__main__': main()