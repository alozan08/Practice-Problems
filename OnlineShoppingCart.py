class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def set_name(self, item_name):
        self.item_name = item_name

    def set_price(self, item_price):
        self.item_price = item_price

    def set_quantity(self, item_quantity):
        self.item_quantity = item_quantity

    def set_description(self, item_description):
        self.item_description = item_description

    def get_name(self):
        return self.item_name

    def get_price(self):
        return self.item_price

    def get_quantity(self):
        return self.item_quantity

    def get_description(self):
        return self.item_description

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1,2016",cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.get_name() == item_name:
                self.cart_items.remove(item)
                return
        print('Item not found in cart. Nothing removed.')

    def modify_item(self, item_name, qty):
        for item in self.cart_items:
            if item.get_name() == item_name:
                item.set_quantity(qty)
                return
        print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.get_quantity()
        return total

    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.get_price() * item.get_quantity()
        return total

    def print_total(self):
        num = self.get_num_items_in_cart()
        self.title()
        if self.get_num_items_in_cart() == 0:
            print(f'Number of Items: {num}\n')
            print("SHOPPING CART IS EMPTY\n")
            print(f'Total: ${self.get_cost_of_cart()}')

        else:
            print(f"Number of Items: {num}")
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_description(self):
        if self.get_num_items_in_cart() != 0:
            self.title()
            print("Item Descriptions")
            for item in self.cart_items:
                item.print_item_description()

    def title(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")


def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print()

def execute_menu(choice, cart):
    print()
    match choice:
        case "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = int(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, desc))
        case "r":
            print("REMOVE ITEM FROM CART")
            rem = input("Enter name of item to remove:\n")
            cart.remove_item(rem)
        case "c":
            print("CHANGE ITEM QUANTITY")
            change = input("Enter the item name:\n")
            qty = int(input("Enter the new quantity:\n"))
            cart.modify_item(change, qty)
        case "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_description()
        case "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()


def user_choice(cart):
    options = ["a", "r", "c", "i", "o", "q"]
    opt = input("Choose an option:\n")

    while opt != 'q':
        if opt not in options:
            opt = input("Choose an option:\n")
            continue
        execute_menu(opt, cart1)
        print_menu()
        opt = input("Choose an option:\n")


if __name__ == "__main__":


    name = input("Enter customer's name:\n")
    date = input("Enter today's date:\n")
    print()

    print(f'Customer name: {name}')
    print(f"Today's date: {date}")
    print()

    cart1 = ShoppingCart(name, date)
    print_menu()
    user_choice(cart1)
