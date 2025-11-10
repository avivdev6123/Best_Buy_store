from products import Product

class Store:
    products_list = []
    def __init__(self, product_list):
        self.products_list = product_list

    def add_product(self, product):
        if isinstance(product, Product):
            self.products_list.append(product)

    def remove_product(self, product):
        new_product_list = []
        if isinstance(product, Product):
            for item in self.products_list:
                if not item.name == product.name:
                    new_product_list.append(item)
            self.products_list = new_product_list
        else:
            print("the item you are trying to remove is not Product type")

    def show_store_catalog(self):
        print("------")
        for index in range(len(self.products_list)):
            print(f"{index+1}. {self.products_list[index].name}, Price: {self.products_list[index].price},"
                  f" Quantity: {self.products_list[index].quantity}")
        print("------\n")

    def get_total_amount(self) -> float:
        total_amount = 0
        for product in self.products_list:
            total_amount += product.price * product.quantity
        return total_amount

    def get_total_quantity(self) -> int:
        total_items = 0
        for product in self.products_list:
            total_items = total_items + product.quantity
        return total_items

    def get_all_active_products(self):
        active_products = []
        for product in self.products_list:
            if product.active:
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        order_total_amount = 0
        for product in self.get_all_active_products():
            for product_order, quantity_order in shopping_list:
                if product.name == product_order.name:
                    order_total_amount = order_total_amount + product.buy(quantity_order)
        return order_total_amount


