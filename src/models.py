class Product:
    """
    Класс для представления товара.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        Args:
            name (str): Название товара
            description (str): Описание товара
            price (float): Цена товара
            quantity (int): Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для цены с проверкой."""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового товара.

        Args:
            product_data (dict): Словарь с данными товара

        Returns:
            Product: Созданный объект товара
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        return cls(name, description, price, quantity)


class Category:
    """
    Класс для представления категории товаров.
    """

    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        Args:
            name (str): Название категории
            description (str): Описание категории
            products (list): Список товаров категории
        """
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        """
        Добавляет товар в категорию.

        Args:
            product (Product): Объект товара для добавления
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров в формате одной строки."""
        products_str = ""
        for product in self.__products:
            products_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return products_str.rstrip()  # Убираем последний перенос строки

    # Добавляем свойство для обратной совместимости со старой функциональностью
    @property
    def products_list(self):
        """Свойство для обратной совместимости - возвращает список товаров."""
        return self.__products

    @property
    def current_category_count(self):
        """Текущее количество категорий."""
        return Category.category_count

    @property
    def current_product_count(self):
        """Текущее количество товаров."""
        return Category.product_count

    # Для обратной совместимости со старой функциональностью
    def __len__(self):
        """Возвращает количество товаров в категории (для обратной совместимости)."""
        return len(self.__products)
