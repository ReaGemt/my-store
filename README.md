# My Store

## Описание

My Store — это простая система управления ассортиментом товаров для сети магазинов. 
Программа позволяет добавлять, удалять, обновлять товары и получать их цены. Также можно вывести список 
всех товаров в магазине с их ценами.

## Функциональные возможности

- Добавление товара в ассортимент магазина
- Удаление товара из ассортимента магазина
- Обновление цены товара
- Получение цены товара по его названию
- Вывод списка всех товаров в магазине

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/ReaGemt/taskmanager.git
    ```

2. Перейдите в папку проекта:

    ```bash
    cd taskmanager
    ```

## Использование

Создайте объекты класса `Store` и используйте методы для управления ассортиментом товаров.

### Пример использования

```python
# Импортируем класс Store
from store import Store

# Создаем объекты класса Store
store1 = Store('Перекресток', 'Россия, г. Пенза, Улица Пушкина, дом 2')
store2 = Store('Чижик', 'Россия, г. Москва, Улица Ленина, дом 5')
store3 = Store('Пятерочка', 'Россия, г. Санкт-Петербург, Улица Мира, дом 10')

# Добавляем товары в магазин Перекресток
store1.add_item('груши', 120.99)
store1.add_item('яблоки', 90.5)
store1.add_item('апельсины', 160.99)
store1.add_item('бананы', 200.5)

# Выводим список товаров в магазине Перекресток
store1.list_items()

# Удаляем товар "яблоки" из магазина Перекресток
store1.remove_item('яблоки')

# Получаем цену товара "апельсины" из магазина Перекресток
print(f'Цена апельсинов: {store1.get_item_price("апельсины")}')

# Обновляем цену товара "груши" в магазине Перекресток
store1.update_item_price('груши', 130.0)

# Повторный вывод списка товаров в магазине Перекресток
store1.list_items()

print('=' * 40)  # Разделитель между магазинами

# Добавляем товары в магазин Чижик
store2.add_item('молоко', 60.0)
store2.add_item('хлеб', 35.0)

# Выводим список товаров в магазине Чижик
store2.list_items()

# Удаляем товар "хлеб" из магазина Чижик
store2.remove_item('хлеб')

# Получаем цену товара "молоко" из магазина Чижик
print(f'Цена молока: {store2.get_item_price("молоко")}')

# Обновляем цену товара "молоко" в магазине Чижик
store2.update_item_price('молоко', 65.0)

# Повторный вывод списка товаров в магазине Чижик
store2.list_items()

print('=' * 40)  # Разделитель между магазинами

# Добавляем товары в магазин Пятерочка
store3.add_item('яйца', 90.0)
store3.add_item('сыр', 250.0)

# Выводим список товаров в магазине Пятерочка
store3.list_items()

# Удаляем товар "яйца" из магазина Пятерочка
store3.remove_item('яйца')

# Получаем цену товара "сыр" из магазина Пятерочка
print(f'Цена сыра: {store3.get_item_price("сыр")}')

# Обновляем цену товара "сыр" в магазине Пятерочка
store3.update_item_price('сыр', 260.0)

# Повторный вывод списка товаров в магазине Пятерочка
store3.list_items()

print('=' * 40)  # Разделитель между магазинами
```

## Тестирование
Вы можете протестировать функциональность класса Store, используя предоставленные примеры. 
Убедитесь, что все методы работают корректно и выводят ожидаемые результаты.

## Лицензия
Этот проект лицензирован под лицензией MIT. Подробности смотрите в файле LICENSE.