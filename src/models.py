from abc import ABC, abstractmethod


class LoggingMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        """Инициализация с логированием параметров."""
        super().__init__(*args, **kwargs)
        class_name = self.__class__.__name__
        print(f"Создан объект {class_name} с параметрами: {args}")

    def __repr__(self):
        """Представление объекта для отладки."""
        attributes = []
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                attributes.append(f"{attr}='{value}'" if isinstance(value, str) else f"{attr}={value}")
        return f"{self.__class__.__name__}({', '.join(attributes)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для товаров."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Абстрактный метод инициализации продукта."""
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Абстрактный сеттер для цены."""
        pass


class Product(LoggingMixin, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара в наличии
        """
        super().__init__(name, description, price, quantity)
        self.__price = price

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение продуктов.

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
            product_data: Словарь с данными товара

        Returns:
            Product: Созданный объект товара
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        return cls(name, description, price, quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Инициализация смартфона.

        Args:
            name: Название смартфона
            description: Описание смартфона
            price: Цена смартфона
            quantity: Количество на складе
            efficiency: Производительность
            model: Модель смартфона
            memory: Объем встроенной памяти (ГБ)
            color: Цвет смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """Строковое представление смартфона."""
        return (f"{self.name} ({self.model}), {self.price} руб. "
                f"Остаток: {self.quantity} шт. Память: {self.memory}ГБ, "
                f"Цвет: {self.color}")


class LawnGrass(Product):
    """Класс для представления травы газонной."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        """
        Инициализация травы газонной.

        Args:
            name: Название травы
            description: Описание травы
            price: Цена травы
            quantity: Количество на складе
            country: Страна-производитель
            germination_period: Срок прорастания (дни)
            color: Цвет травы
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """Строковое представление травы газонной."""
        return (f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт. "
                f"Страна: {self.country}, "
                f"Прорастание: {self.germination_period} дней")


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров категории
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
            TypeError: Если объект не является продуктом
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product "
                          "или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер для списка товаров в формате одной строки."""
        products_str = "\n".join(str(product) for product in self.__products)
        return products_str

    @property
    def products_list(self):
        """Свойство для обратной совместимости."""
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
    """Вспомогательный класс для итерации по товарам категории."""

    def __init__(self, products: list):
        """
        Инициализация итератора.

        Args:
            products: Список товаров категории
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
