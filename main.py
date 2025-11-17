from src.models import Product, Category, Smartphone, LawnGrass

if __name__ == "__main__":
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    # Создание обычных продуктов (старая функциональность)
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

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

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_list))
    print(category1.category_count)
    print(category1.product_count)

    # Новая функциональность - создание смартфонов
    smartphone1 = Smartphone("iPhone 15 Pro", "Флагманский смартфон", 120000.0, 10,
                             efficiency=4.5, model="15 Pro", memory=256, color="Титановый")

    smartphone2 = Smartphone("Samsung Galaxy S24", "Ультрасовременный смартфон", 90000.0, 15,
                             efficiency=4.8, model="S24 Ultra", memory=512, color="Черный")

    print("\nСмартфоны (новые классы):")
    print(smartphone1)
    print(smartphone2)

    # Новая функциональность - создание травы газонной
    grass1 = LawnGrass("Газонная трава Премиум", "Высококачественная газонная трава", 2500.0, 50,
                       country="Германия", germination_period=14, color="Ярко-зеленый")

    grass2 = LawnGrass("Спортивный газон", "Трава для спортивных площадок", 1800.0, 30,
                       country="Нидерланды", germination_period=10, color="Темно-зеленый")

    print("\nТрава газонная (новые классы):")
    print(grass1)
    print(grass2)

    # Демонстрация сложения товаров одного типа
    print("\nСложение смартфонов:")
    try:
        smartphone_total = smartphone1 + smartphone2
        print(f"Общая стоимость смартфонов: {smartphone_total} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\nСложение травы газонной:")
    try:
        grass_total = grass1 + grass2
        print(f"Общая стоимость травы: {grass_total} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Демонстрация ошибки при сложении разных типов
    print("\nПопытка сложить смартфон и траву:")
    try:
        invalid_total = smartphone1 + grass1
        print(f"Результат: {invalid_total} руб.")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Создание категорий с новыми товарами
    smartphones_category = Category("Смартфоны", "Мобильные устройства", [smartphone1, smartphone2])
    grass_category = Category("Газонная трава", "Садовые товары", [grass1, grass2])

    print(f"\nКатегория смартфонов: {smartphones_category}")
    print("Товары в категории смартфонов:")
    for product in smartphones_category:
        print(f"  - {product}")

    print(f"\nКатегория травы: {grass_category}")
    print("Товары в категории травы:")
    for product in grass_category:
        print(f"  - {product}")

    # Демонстрация защиты метода add_product
    print("\nПопытка добавить не-продукт в категорию:")
    try:
        smartphones_category.add_product("не продукт")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Корректное добавление продукта
    print("\nКорректное добавление продукта:")
    smartphone3 = Smartphone("Google Pixel 8", "Смартфон с AI", 75000.0, 8,
                             efficiency=4.2, model="Pixel 8", memory=128, color="Белый")
    smartphones_category.add_product(smartphone3)
    print(f"После добавления: {smartphones_category}")
    print("Товары в категории:")
    for product in smartphones_category:
        print(f"  - {product}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products_list))
    print(category2.products)

    print(f"\nОбщая статистика:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
