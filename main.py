from products import Product
from store import Store

MENU = {
    "1": "List all products in store",
    "2": "Show total amount in store",
    "3": "Make an order",
    "4": "Quit"
}

def show_menu():
    print("   Store Menu\n   ----------")
    for item in MENU.keys():
        print(f"{item}. {MENU[item]}")

def start(store):
    while True:
        show_menu()
        choice = input("Please choose a number: ")
        if choice not in MENU.keys():
            continue
        elif choice == "1":
            store.show_store_catalog()

        elif choice == "2":
            print(f"Total of {store.get_total_quantity()} items in store\n")

        elif choice == "3":
            order_list = []
            store.show_store_catalog()
            print("When you want to finish order, enter empty text.")
            while True:
                product_choice = input("Which product # do you want? ")
                product_quantity = input("What amount do you want? ")
                if (product_choice == "" or product_choice == None):
                    break

                try:
                    selected_index = int(product_choice)
                    selected_quantity = int(product_quantity)

                    if 1 <= selected_index <= len(store.get_all_active_products()):
                        item_tuple = (store.products_list[selected_index-1], selected_quantity)
                        order_list.append(item_tuple)
                        print("Product added to list!\n")
                    else:
                        print("please select a product # from the list!")

                except ValueError as a:
                    print(f"Error adding product!, error message: {a}\n")

            if order_list:
                total_order_amount = store.order(order_list)
                print(f"Order made! Total payment: {total_order_amount}\n")


def main():
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()