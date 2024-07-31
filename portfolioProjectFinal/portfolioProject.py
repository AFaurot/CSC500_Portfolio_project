import datetime

class ItemToPurchase:

    #Constructor with initial values and defines types
    def __init__(self, item_name="none", item_price=float(0), item_quantity=int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    #Function to format and print the items cost and return the items total

    #leaving function in for Milestone 1 submission. A better function in in shopping cart class for final project
    def print_item_cost(self):
        item_total = round(self.item_price * self.item_quantity, 2)
        print('{} {} @ ${} = ${}'.format(self.item_name, self.item_quantity, self.item_price, item_total))
        return item_total


class ShoppingCart:

    cart_items = []
    item_description = {}
    item_price = {}
    cart_item_quantity ={}

    # Constructor with initial values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date


    #function to add items to the ShoppingCart dictionaries and cart_items list
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase.item_name)
        description = input("Enter description of {} ".format(item_to_purchase.item_name))
        self.item_description[item_to_purchase.item_name] = description
        self.item_price[item_to_purchase.item_name] = item_to_purchase.item_price
        self.cart_item_quantity[item_to_purchase.item_name] = item_to_purchase.item_quantity

    def remove_item(self, item_to_del):
        if item_to_del not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else:
            self.cart_items.remove(item_to_del)

    def modify_item(self, item_to_purchase):
        if item_to_purchase not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else:
            print("Modification MENU \n d = Description \n p=price \n q= quantity")

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

def main():

    #Leaving in submission for Milestone 1:

    print("------------BEGIN SUBMISSION FOR MILESTONE 1------------\n")
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
    #End of milestone 1
    print("\n------------END SUBMISSION FOR MILESTONE 1------------\n")

    #Begin main portfolio project by initializing shopping cart based on todays date and customer_name
    print("------------BEGIN SUBMISSION FOR FINAL PROJECT------------\n")
    customer_name = input("Enter your name: ")
    today = str(datetime.date.today())
    sc = ShoppingCart(customer_name, today)
    print("Customer Name : ", customer_name)
    print("Today's Date : ", today)

    def print_menu():
        print("\nMenu \na = Add item to cart \nr = Remove item from cart")
        print("c = Change item quantity \ni = Output items' descriptions")
        print("o = Output shopping cart \nq = Quit\n")
        command = input("Enter command :")
        #total = 0
        while command != 'q':

            if command == 'a':
                item_name = input("Enter the item name: ")
                if item_name in sc.cart_items:
                    print("item already exists in cart")
                else:
                    item_cost = float(input("Enter the item price: "))
                    item_quantity = int(input("Enter the item quantity: "))
                    item = ItemToPurchase(item_name, item_cost, item_quantity)
                #    total += (ItemToPurchase.print_item_cost(item)[0])
                 #   formatted_list.append((ItemToPurchase.print_item_cost(item)[1]))
                    sc.add_item(item)
                    #ShoppingCart.cart_item_quantity += item_quantity
            ##To be implemented later in week 8
            elif command == 'r':
                pass
            ##To be implemented later in week 8
            elif command == 'c':
                pass
            ##print descriptions
            elif command == 'i':
                #pass
                sc.print_descriptions()
            ##Print cart output
            elif command == 'o':
               print("Testing cart item list" , sc.cart_items)
               print("Testing cart price", sc.item_price)
               print("Testing cart quantity", sc.cart_item_quantity)
               # sc.print_total()
               # print_formatted_list()
                #add Initial total from milestone 1 to total on milestone2
               # print("Total: ${}".format(init_total + total))

            #Catch invalid input and prompt for correct input
            else:
                print("Invalid command")
                print("\nMenu \na = Add item to cart \nr = Remove item from cart")
                print("c = Change item quantity \ni = Output items' descriptions")
                print("o = Output shopping cart \nq = Quit\n")
            command = input("Enter command :")

    print_menu()


if __name__ == '__main__': main()