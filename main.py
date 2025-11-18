from src.models import Product, Category, Smartphone, LawnGrass

if __name__ == "__main__":
    # Сброс счетчиков
    Category.category_count = 0
    Category.product_count = 0

    print("=== Создание продуктов с логированием ===")

    # Создание продуктов (будет видно логирование)
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    print("\n=== Создание смартфонов и травы ===")

    smartphone1 = Smartphone("iPhone 15 Pro", "Флагманский смартфон",
                             120000.0, 10, 4.5, "15 Pro", 256, "Титановый")

    grass1 = LawnGrass("Газонная трава Премиум", "Высококачественная трава",
                       2500.0, 50, "Германия", 14, "Ярко-зеленый")

    print("\n=== Демонстрация repr ===")
    print(f"Repr продукта: {repr(product1)}")
    print(f"Repr смартфона: {repr(smartphone1)}")
    print(f"Repr травы: {repr(grass1)}")

    print("\n=== Основная функциональность ===")

    # Старая функциональность
    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category("Смартфоны", "Смартфоны для коммуникации",
                         [product1, product2, smartphone1])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products_list))
    print(category1.current_category_count)
    print(category1.current_product_count)

    # Создание второй категории
    product3 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры", "Современные телевизоры", [product3])

    print(category2.name)
    print(category2.description)
    print(len(category2.products_list))

    print(f"\nВсего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
