from src.models import Product, Category


def main():
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("Информация о продуктах:")
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    # Создание категории смартфоны
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.current_category_count)
    print(category1.current_product_count)

    # Создание товара через класс-метод и добавление в категорию
    product_data = {
        'name': 'Google Pixel 8',
        'description': '128GB, Черный',
        'price': 150000.0,
        'quantity': 3
    }
    product4 = Product.new_product(product_data)
    category1.add_product(product4)

    # Демонстрация форматированного вывода товаров
    print("\nТовары в категории Смартфоны:")
    for product_info in category1.products:
        print(product_info)

    # Демонстрация работы с ценой
    print(f"\nИзменение цены {product1.name}:")
    print(f"Текущая цена: {product1.price} руб.")

    # Попытка установить невалидную цену
    product1.price = -100

    # Корректное изменение цены
    product1.price = 190000.0
    print(f"Новая цена: {product1.price} руб.")

    # Создание второй категории
    product5 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product5])

    print(f"\n{category2.name}")
    print(category2.description)
    print(len(category2.products))

    # Демонстрация форматированного вывода для телевизоров
    print("Товары в категории Телевизоры:")
    for product_info in category2.products:
        print(product_info)

    print(f"\nОбщая статистика:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


if __name__ == "__main__":
    main()
