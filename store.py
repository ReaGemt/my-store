class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


# Создание магазинов (название и адрес магазина) на примере X5 retail group
store1 = Store('Перекресток','Россия, г. Пенза, Улица Пушкина, дом 2')
# Выводим название и адрес магазина
print(f'Имя магазина: {store1.name}')
print(f'Адрес магазина: {store1.address}')

# Добавление товаров в магазины 1
store1.add_item("Вода ""Святой Источник", 24.0)
store1.add_item("bananas", 0.75)

# Тестирование методов на store1
store1.add_item("oranges", 1.2)
print(store1.items)  # Проверка добавления товара

store1.update_price("apples", 0.6)
print(store1.items)  # Проверка обновления цены товара

store1.remove_item("bananas")
print(store1.items)  # Проверка удаления товара

print(store1.get_price("apples"))  # Проверка получения цены товара
print(store1.get_price("bananas"))  # Проверка получения цены товара, который был удален

store2 = Store("Чижик", "456 Market St")
# Выводим название и адрес магазина
print(f'Имя магазина: {store1.name}')
print(f'Адрес магазина: {store1.address}')

# Добавление товаров в магазины 2
store2.add_item("milk", 1.5)
store2.add_item("bread", 2.0)

store3 = Store("Пятерочка", "789 Broadway St")
# Выводим название и адрес магазина
print(f'Имя магазина: {store1.name}')
print(f'Адрес магазина: {store1.address}')

# Добавление товаров в магазины 3
store3.add_item("eggs", 3.0)
store3.add_item("cheese", 4.0)






# Тестирование методов на store2
store2.get_price("milk")  # Проверка получения цены несуществующего товара

# Тестирование методов на store3
store3.get_price("eggs")  # Проверка получения цены несуществующего товара

# Тестирование методов на store3
store3.get_price("eggs")  # Проверка получения цены несуществующего товара

# Тестирование методов на store3
store3.get_price("eggs")  # Проверка получения цены несуществующего товара



# Выводим список товаров в магазине
store1.add_item()
