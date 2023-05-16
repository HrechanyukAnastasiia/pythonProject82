class Clothing:
    def __init__(self, material, name, price, size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self, item):
        self.inventory.append(item)
    def remove_item(self, item):
        self.inventory.remove(item)
    def get_items(self):
        return self.inventory
    def search_items(self, key):
        return [item for item in self.inventory if key in item.name]


class Customer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.cart = []
    def add_to_cart(self,item):
        if item.price <= self.budget:
            self.cart.append(item)
            self.budget -= item.price
            print(f'{item.name} додано до кошика')
        else:
            print('Недостатньо коштів')
    def remove_from_cart(self, item):
        if item in self.cart:
            self.cart.remove(item)
            self.budget += item.price
            print(f'{item.name} видалено з кошика')
        else:
            print(f'{item.name} немає в кошику')
    def view_cart(self):
        if len(self.cart) == 0:
            print('Кошик порожній')
        else:
            print('Кошик:')
            for item in self.cart:
                print(f'{item.name} ({item.size}): {item.price}')
    def checkout(self):
        total_price = sum(item.price for item in self.cart)
        if total_price <= self.budget:
            self.cart = []
            self.budget -= total_price
            print('Оплата пройшла успішно!')
        else:
            print('Недостатньо коштів для оформлення замовлення.')


shop = Store("LC WAIKIKI", "вулиця 600-річчя")
print(shop.name + ', ' + shop.address)
shop.add_item(Clothing("Бавовна", "Футболка", 10, "M"))
shop.add_item(Clothing("Вовна", "Шорти", 40, "XL"))
shop.add_item(Clothing("Поліестр", "Майка", 100, "L"))
print()

customer = Customer("Настя", 10)
print(f"Покупець: {customer.name}, Баланс: {customer.budget}")
print()
results = shop.search_items("Шорти")
if results:
    customer.add_to_cart(results[0])
results1 = shop.search_items("Майка")
if results:
    customer.add_to_cart(results1[0])

customer.view_cart()
customer.remove_from_cart(results[0])
customer.remove_from_cart(results1[0])
customer.view_cart()
print()
customer.checkout()