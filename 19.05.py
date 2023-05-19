class Clothing:
    def __init__(self , material , name , price , size):
        self.material = material
        self.name = name
        self.price = price
        self.size = size

class Store:
    def __init__(self , name , address):
        self.name = name
        self.address = address
        self.inventory = []
    def add_item(self , item):
        self.inventory.append(item)
    def remove_item(self , item):
        self.inventory.remove(item)
    def get_items(self ):
        return self.inventory
    def search_items(self , key):
        dictionary = []
        for dict in self.inventory:
            if key in dict.name:
                dictionary.append(key)
        for value in dictionary:
            if len(dictionary) == 0:
                print(f"Немає {key} в наявності")
            else:
                print(f"Ось що ми знайшли по Вашому запиту: {value}")

class Customer:
    def __init__(self , name, budget):
        self.name = name
        self.budget = budget
        self.cart = []

    def add_to_cart(self , item):
        if item.price <= self.budget:
         self.cart.append(item)
         print(f"{item.name} {item.size} -> ({item.price} грн) була добавлена в корзину")
        else:
            print("У вас не достатньо коштів")
    def view_cart(self):
      if len(self.cart) == 0:
          print("У вас пусто в корзині")
      else:
        print("\nКорзина:")
        for dictionary in self.cart:
         print(f"{dictionary.name} {dictionary.size} -> {dictionary.price}")

    def remove_from_cart(self , item):
        self.cart.remove(item)
        print(f"\n{item.name} {item.size} -> була видалена з корзини")
    def checkout(self):
        count = 0
        if len(self.cart) == 0:
            print("У вас пусто в карзині")
        else:
            print("\nПокупки:")
            for dictionary in self.cart:
                 print(f"{dictionary.name} {dictionary.size} -> {dictionary.price}")
                 count += dictionary.price
            print(f"Сума: {count}")



shop = Store("LC WAIKIKI", "вулиця 600-річчя")
item_1 = Clothing("Кожа" , "Куртка" , 500 , "XL")
item_2 = Clothing("Хлопок" , "Кофта"  , 400 , "L")
shop.add_item(item_1)
shop.add_item(item_2)
customer = Customer("Настя" , 1000)
customer.add_to_cart(item_1)
customer.add_to_cart(item_2)
customer.view_cart()
customer.checkout()
shop.search_items("Куртка")
shop.search_items("Кофта")