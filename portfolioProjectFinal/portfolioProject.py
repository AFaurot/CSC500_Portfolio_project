import datetime


class ItemToPurchase:

    # Constructor with initial values and type definitions
    def __init__(self, item_name="none", item_price=float(0), item_quantity=int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # print_item_cost() to format and print the items cost and return the items total
    # I am leaving this function in for Milestone 1 submission.
    # A better function is print_total() in ShoppingCart class for the final project'''
    def print_item_cost(self):
        item_total = round(self.item_price * self.item_quantity, 2)
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, item_total))
        return item_total


class ShoppingCart:

    # cart_items will serve as the key for all values in description, price, and quantity dictionaries.
    # Each value in cart items is unique after the milestone one submission.
    cart_items = []
    item_description = {}
    item_price = {}
    cart_item_quantity ={}

    # Constructor with initial values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date

    # function to add items to the ShoppingCart dictionaries and cart_items list
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase.item_name)
        description = input("Enter description of {} ".format(item_to_purchase.item_name))
        self.item_description[item_to_purchase.item_name] = description
        self.item_price[item_to_purchase.item_name] = item_to_purchase.item_price
        self.cart_item_quantity[item_to_purchase.item_name] = item_to_purchase.item_quantity

    # function to remove item from ShoppingCart dictionaries and cart_items list
    def remove_item(self, item_to_del):
        if item_to_del not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else:
            del self.cart_item_quantity[item_to_del]
            del self.item_price[item_to_del]
            del self.item_description[item_to_del]
            self.cart_items.remove(item_to_del)

    # Function to modify item in cart
    def modify_item(self, item_to_purchase):
        if item_to_purchase not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else:
            print("Modification MENU \n d = Description \n p = price \n n = quantity \n q = exit")
            command = input("Enter Command : ")
            while command != 'q':
                if command == 'd':
                    new_desc = input("Enter new description for {} : ".format(item_to_purchase))
                    self.item_description[item_to_purchase] = new_desc
                elif command == 'p':
                    #Invalid type error handling
                    while True:
                        try:
                            new_price = float(input("Enter new price for {} : ".format(item_to_purchase)))
                            self.item_price[item_to_purchase] = new_price
                            break
                        except:
                            print("INVALID INPUT: Please enter a numerical value")
                elif command == 'n':
                    # Invalid type error handling
                    while True:
                        try:
                            new_quantity = int(input("Enter new quantity for {} : ".format(item_to_purchase)))
                            self.cart_item_quantity[item_to_purchase] = new_quantity
                            break
                        except:
                            print("INVALID INPUT: Please enter a numerical value")
                else:
                    print("Invalid command")
                print("Modification MENU \n d = Description \n p = price \n n = quantity \n q = exit")
                command = input("Enter Command : ")

    # Function to return quantity of items in cart as a sum
    def get_num_items_in_cart(self):
        return sum(self.cart_item_quantity.values())

    # Function to get cost of cart
    # Iterates over length of cart_items
    # Uses value of cart_items list at index for keys in dictionaries cart_item_quantity and item_price
    # This ensures that the correct cart items are multiplying quantity * price

    def get_cost_of_cart(self):
        total_cost = float(0)
        index = 0
        for i in range(len(self.cart_items)):
            total_cost += (self.cart_item_quantity[self.cart_items[index]]) * (self.item_price[self.cart_items[index]])
            index += 1
        return round(total_cost, 2)

    # Function to print descriptions of items in cart
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions :")
        for item, desc in self.item_description.items() :
            print("{} : {}".format(item, desc))

    # Function to print total. Similar logic for using cart_items at index for dict keys
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            index = 0
            for item in self.cart_items:
                line_total = float(round((self.cart_item_quantity[self.cart_items[index]]
                                          * self.item_price[self.cart_items[index]]), 2))
                print("{} {} @ ${} = ${}".format(item,self.cart_item_quantity[self.cart_items[index]],
                                                 self.item_price[self.cart_items[index]], line_total))
                index += 1
            total = self.get_cost_of_cart()
            print("Total is : ${}".format(total))


# Print menu function to reduce amount of code used for printing the menu
def print_menu():
    print("\n----MENU---- \na = Add item to cart \nr = Remove item from cart")
    print("c = Change item quantity, description, or price \ni = Output items' descriptions")
    print("o = Output shopping cart \nq = Quit\nm = Print this menu\n")


def main():

    # Leaving in submission for Milestone 1:

    print("------------BEGIN SUBMISSION FOR MILESTONE 1------------\n")
    item1_name = input("Enter the item name: ")
    item1_cost = float(input("Enter the item price: "))
    item1_quantity = int(input("Enter the item quantity: "))
    # pass item1 to ItemToPurchase class
    item1 = ItemToPurchase(item1_name, item1_cost, item1_quantity)
    item2_name = input("Enter the item name: ")
    item2_cost = float(input("Enter the item price: "))
    item2_quantity = int(input("Enter the item quantity: "))
    # pass item2 to ItemToPurchase class
    item2 = ItemToPurchase(item2_name, item2_cost, item2_quantity)
    print("TOTAL COST")
    # Variable to ItemToPurchase.print_item_cost() for both items and add the result
    init_total = (ItemToPurchase.print_item_cost(item1) + ItemToPurchase.print_item_cost(item2))
    print("Total: ${}".format(init_total))
    # End of milestone 1
    print("\n------------END SUBMISSION FOR MILESTONE 1------------\n")

    # Begin main portfolio project by initializing shopping cart based on today's date and customer_name
    print("------------BEGIN SUBMISSION FOR FINAL PROJECT------------\n")
    customer_name = input("\nEnter your name: ")
    today = str(datetime.date.today())
    sc = ShoppingCart(customer_name, today)
    print("Customer Name : ", customer_name)
    print("Today's Date : ", today)

    # Add an option to add Milestone 1 items to the cart.
    # I am not allowing duplicate entries for the cart_items list in ShoppingCart class.
    # Duplicate items in the list could break the flow of logic.

    add_milestone1_items = input("\nWould you like to add Milestone 1 items to the shopping cart?\n"
                                 "Please note that this will only work if each item name was unique."
                                 " y = yes any other character = no ")
    if add_milestone1_items == 'y' and item1.item_name != item2.item_name:
        sc.add_item(item1)
        sc.add_item(item2)
    else:
        print("Your input was '{}'. "
              "Milestone 1 items not added to the cart".format(add_milestone1_items))

    # Function to run the main code logic. Prints menu and prompts for user input
    def run_looping_menu():
        print_menu()
        command = input("Enter command :")
        # Loop will run until user presses 'q'
        while command != 'q':

            # Add item to cart, ensuring unique key in sc.cart_items
            if command == 'a':
                item_name = input("Enter the item name: ")
                if item_name in sc.cart_items:
                    print("item already exists in cart")
                else:
                    while True:
                        # Invalid Type error handling
                        try:
                            item_cost = float(input("Enter the item price: "))
                            break
                        except:
                            print("INVALID INPUT: Please enter a numerical value")
                    while True:
                        # Invalid Type error handling
                        try:
                            item_quantity = int(input("Enter the item quantity: "))
                            break
                        except:
                            print("INVALID INPUT: Please enter an integer value:")
                    item = ItemToPurchase(item_name, item_cost, item_quantity)
                    sc.add_item(item)
            # Remove item from cart
            elif command == 'r':
                item_to_del = input("Enter an item to delete : ")
                sc.remove_item(item_to_del)
            elif command == 'c':
                item_to_modify = input("Enter an item to modify : ")
                sc.modify_item(item_to_modify)
            # Print descriptions
            elif command == 'i':
                sc.print_descriptions()
            # Print cart output
            elif command == 'o':
                sc.print_total()
            # Print options menu
            elif command == 'm':
                print_menu()
            # Let user know about wrong input
            else:
                print("Invalid command, make sure there are no whitespaces after your input\n")
            command = input("Enter next command (m for the command menu):")
    # Run the main menu logic of the code
    run_looping_menu()


if __name__ == '__main__': main()