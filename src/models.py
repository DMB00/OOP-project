class Product:
    """
    Базовый класс для представления товара.
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
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение продуктов - возвращает общую стоимость всех товаров на складе.

        Args:
            other (Product): Другой продукт для сложения

        Returns:
            float: Общая стоимость товаров на складе
        """
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных типов")

        return (self.price * self.quantity) + (other.price * other.quantity)

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


class Smartphone(Product):
    """
    Класс для представления смартфона.
    Наследуется от класса Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Инициализация смартфона.

        Args:
            name (str): Название смартфона
            description (str): Описание смартфона
            price (float): Цена смартфона
            quantity (int): Количество на складе
            efficiency (float): Производительность
            model (str): Модель смартфона
            memory (int): Объем встроенной памяти (ГБ)
            color (str): Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона."""
        return (f"{self.name} ({self.model}), {self.price} руб. Остаток: {self.quantity} шт. "
                f"Память: {self.memory}ГБ, Цвет: {self.color}")


class LawnGrass(Product):
    """
    Класс для представления травы газонной.
    Наследуется от класса Product.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        """
        Инициализация травы газонной.

        Args:
            name (str): Название травы
            description (str): Описание травы
            price (float): Цена травы
            quantity (int): Количество на складе
            country (str): Страна-производитель
            germination_period (int): Срок прорастания (дни)
            color (str): Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление травы газонной."""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Страна: {self.country}, Прорастание: {self.germination_period} дней")


class Category:
    """
    Класс для представления категории товаров.
    """

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
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """
        Добавляет товар в категорию.

        Args:
            product: Объект товара для добавления

        Raises:
            TypeError: Если переданный объект не является продуктом или его наследником
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров в формате одной строки."""
        products_str = "\n".join(str(product) for product in self.__products)
        return products_str

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

    def __len__(self):
        """Возвращает количество товаров в категории."""
        return len(self.__products)

    def __iter__(self):
        """Возвращает итератор для перебора товаров категории."""
        return CategoryIterator(self.__products)


class CategoryIterator:
    """
    Вспомогательный класс для итерации по товарам категории.
    """

    def __init__(self, products: list):
        """
        Инициализация итератора.

        Args:
            products (list): Список товаров категории
        """
        self.products = products
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект как итератор."""
        return self

    def __next__(self):
        """
        Возвращает следующий товар в категории.

        Returns:
            Product: Следующий товар

        Raises:
            StopIteration: Когда товары закончились
        """
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
