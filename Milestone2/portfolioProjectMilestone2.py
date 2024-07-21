class ItemToPurchase:
    #Constructor with initial values and defines types
    def __init__(self, item_name="none", item_price=float(0), item_quantity=int(0)):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity


    #Function to format and print the items cost and return the items total
    def print_item_cost(self):
        item_total = round(self.item_price * self.item_quantity, 2)
        output = (('{} {} @ ${} = ${}'.format
                                    (self.item_name,
                                     self.item_quantity,
                                     self.item_price,
                                     item_total)))

        #Return list object so items are easy to unpack
        return [item_total, output]


class ShoppingCart:
    cart_items = []
    item_description = {}
    cart_item_quantity = 0
    # Constructor with initial values
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        #self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
        description =input("Enter description of {} ".format(item_to_purchase))
        self.item_description[item_to_purchase]=description
    def remove_item(self, item_to_del):
        if item_to_del not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else:
            self.cart_items.remove(item_to_del)

    #modify_item is partially implemented. Will be finished in week 8
    def modify_item(self, item_to_purchase):
        if item_to_purchase not in self.cart_items:
            print("Item not found in cart. Nothing modified")
        else :
            print("Modification MENU \n d = Description \n p=price \n q= quantity")

    # stub method to be completed in week 8
    def get_num_items_in_cart(self):
        pass

    # stub method to be completed in week 8
    def get_cost_of_cart(self):
        pass

    # method to print item descriptions
    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions :")
        for item, desc in self.item_description.items() :
            print("{} : {}".format(item, desc))

    # method to print shopping cart total
    def print_total(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        total = self.cart_item_quantity
        if total == 0 :
            print("SHOPPING CART IS EMPTY")
        else :
            print("Number of Items: {}".format(total))



def main ():
    #Formatted list variable used in output
    formatted_list=[]
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
    #add items to my list for formatted output
    formatted_list.append(ItemToPurchase.print_item_cost(item1)[1])
    formatted_list.append(ItemToPurchase.print_item_cost(item2)[1])

    #function to neatly print list
    def print_formatted_list():
        for i in formatted_list:
            print(i)

    print("TOTAL COST")
    print_formatted_list()

    #Variable to ItemToPurchase.print_item_cost() for both items and add the result
    init_total = (ItemToPurchase.print_item_cost(item1)[0] + ItemToPurchase.print_item_cost(item2)[0])

    print("Total: ${}".format(init_total))
    print("\nEnd of output for part 1 of portfolio project.\n")
    sc = ShoppingCart("Aaron Faurot", "07/21/2024")
    sc.add_item(item1_name)
    sc.add_item(item2_name)
    ShoppingCart.cart_item_quantity += item1_quantity
    ShoppingCart.cart_item_quantity += item2_quantity

    def print_menu():
        print("\nMenu \na = Add item to cart \nr = Remove item from cart")
        print("c = Change item quantity \ni = Output items' descriptions")
        print("o = Output shopping cart \nq = Quit\n")
        command = input("Enter command :")
        total = 0
        while command != 'q':
            # Unclear if this implementation of add_item is due this week,
            # I am starting on it regardless.
            # Will be finished in week 8
            if command == 'a':
                item_name = input("Enter the item name: ")
                if item_name in sc.cart_items:
                    print("item already exists in cart")
                else:
                    item_cost = float(input("Enter the item price: "))
                    item_quantity = int(input("Enter the item quantity: "))
                    item = ItemToPurchase(item_name, item_cost, item_quantity)
                    total += (ItemToPurchase.print_item_cost(item)[0])
                    formatted_list.append((ItemToPurchase.print_item_cost(item)[1]))
                    sc.add_item(item_name)
                    ShoppingCart.cart_item_quantity += item_quantity
            ##To be implemented later in week 8
            elif command == 'r':
                pass
            ##To be implemented later in week 8
            elif command == 'c':
                pass
            ##print descriptions
            elif command == 'i':
                sc.print_descriptions()
            ##Print cart output
            elif command == 'o':
                sc.print_total()
                print_formatted_list()
                #add Initial total from milestone 1 to total on milestone2
                print("Total: ${}".format(init_total + total))

            #Catch invalid input and prompt for correct input
            else:
                print("Invalid command")
                print("\nMenu \na = Add item to cart \nr = Remove item from cart")
                print("c = Change item quantity \ni = Output items' descriptions")
                print("o = Output shopping cart \nq = Quit\n")
            command = input("Enter command :")

    print_menu()



if __name__ == '__main__': main()

