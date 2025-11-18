import pytest
from src.models import (Product, Category, Smartphone, LawnGrass,
                        CategoryIterator, BaseProduct, LoggingMixin)


class TestBaseProduct:
    """Тесты для абстрактного базового класса."""

    def test_base_product_is_abstract(self):
        """Тест что BaseProduct является абстрактным классом."""
        # Нельзя создать экземпляр абстрактного класса
        with pytest.raises(TypeError):
            BaseProduct("Test", "Desc", 100.0, 5)

    def test_product_inherits_from_base_product(self):
        """Тест что Product наследуется от BaseProduct."""
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_from_base_product(self):
        """Тест что Smartphone наследуется от BaseProduct через Product."""
        assert issubclass(Smartphone, BaseProduct)

    def test_lawn_grass_inherits_from_base_product(self):
        """Тест что LawnGrass наследуется от BaseProduct через Product."""
        assert issubclass(LawnGrass, BaseProduct)


class TestLoggingMixin:
    """Тесты для класса-миксина."""

    def test_logging_mixin_repr(self):
        """Тест метода __repr__ миксина."""

        class TestClass(LoggingMixin):
            def __init__(self, name, value):
                # Вызываем object.__init__ вместо super()
                object.__init__(self)
                self.name = name
                self.value = value

        obj = TestClass("test_name", 123)
        repr_str = repr(obj)

        assert "TestClass" in repr_str
        assert "name='test_name'" in repr_str
        assert "value=123" in repr_str

    def test_product_has_logging_mixin(self):
        """Тест что Product использует LoggingMixin."""
        product = Product("Test", "Desc", 100.0, 5)
        assert isinstance(product, LoggingMixin)

    def test_logging_on_creation(self, capsys):
        """Тест логирования при создании объекта."""
        product = Product("Test", "Desc", 100.0, 5)
        captured = capsys.readouterr()
        assert "Создан объект Product с параметрами:" in captured.out


class TestProduct:
    """Тесты для класса Product."""

    def test_old_functionality_preserved(self):
        """Тест что старая функциональность сохранена."""
        product = Product("Test", "Desc", 150.0, 5)

        assert product.name == "Test"
        assert product.description == "Desc"
        assert product.price == 150.0
        assert product.quantity == 5

    def test_addition_same_type(self):
        """Тест сложения продуктов одного типа."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)

        total_cost = product1 + product2
        expected_cost = (100.0 * 2) + (200.0 * 3)

        assert total_cost == expected_cost

    def test_addition_different_types(self):
        """Тест сложения продуктов разных типов."""
        product = Product("Product", "Desc", 100.0, 2)
        smartphone = Smartphone("Smartphone", "Desc", 200.0, 3, 4.5, "Model", 128, "Black")

        with pytest.raises(TypeError):
            _ = product + smartphone

    def test_str_representation(self):
        """Тест строкового представления Product."""
        product = Product("Test", "Desc", 100.0, 5)
        expected = "Test, 100.0 руб. Остаток: 5 шт."
        assert str(product) == expected

    def test_price_setter_negative(self, capsys):
        """Тест сеттера цены с отрицательным значением."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = -50
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением."""
        product = Product("Test", "Desc", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_new_product_class_method(self):
        """Тест класс-метода new_product."""
        product_data = {
            'name': 'New Product',
            'description': 'New Desc',
            'price': 100.0,
            'quantity': 5
        }
        product = Product.new_product(product_data)
        assert product.name == 'New Product'
        assert product.description == 'New Desc'
        assert product.price == 100.0
        assert product.quantity == 5

    def test_product_repr(self):
        """Тест метода __repr__ для Product."""
        product = Product("Test", "Desc", 100.0, 5)
        repr_str = repr(product)
        assert "Product" in repr_str
        assert "name='Test'" in repr_str
        assert "description='Desc'" in repr_str


class TestSmartphone:
    """Тесты для класса Smartphone."""

    def test_smartphone_initialization(self):
        """Тест инициализации смартфона."""
        smartphone = Smartphone(
            name="Test Phone",
            description="Test Description",
            price=1000.0,
            quantity=5,
            efficiency=4.5,
            model="Test Model",
            memory=256,
            color="Black"
        )

        assert smartphone.name == "Test Phone"
        assert smartphone.price == 1000.0
        assert smartphone.quantity == 5
        assert smartphone.efficiency == 4.5
        assert smartphone.model == "Test Model"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_smartphone_inheritance(self):
        """Тест что Smartphone наследуется от Product."""
        smartphone = Smartphone("Phone", "Desc", 1000.0, 5, 4.5, "Model", 128, "Black")

        assert isinstance(smartphone, Product)
        assert issubclass(Smartphone, Product)

    def test_smartphone_addition(self):
        """Тест сложения смартфонов."""
        phone1 = Smartphone("Phone1", "Desc1", 1000.0, 2, 4.5, "Model1", 128, "Black")
        phone2 = Smartphone("Phone2", "Desc2", 1500.0, 3, 4.8, "Model2", 256, "White")

        total_cost = phone1 + phone2
        expected_cost = (1000.0 * 2) + (1500.0 * 3)

        assert total_cost == expected_cost

    def test_smartphone_addition_different_type(self):
        """Тест сложения смартфона с другим типом."""
        phone = Smartphone("Phone", "Desc", 1000.0, 2, 4.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 500.0, 5, "Country", 10, "Green")

        with pytest.raises(TypeError):
            _ = phone + grass

    def test_str_representation(self):
        """Тест строкового представления Smartphone."""
        phone = Smartphone("Phone", "Desc", 1000.0, 5, 4.5, "Model", 128, "Black")
        expected = "Phone (Model), 1000.0 руб. Остаток: 5 шт. Память: 128ГБ, Цвет: Black"
        assert str(phone) == expected


class TestLawnGrass:
    """Тесты для класса LawnGrass."""

    def test_lawn_grass_initialization(self):
        """Тест инициализации травы газонной."""
        grass = LawnGrass(
            name="Test Grass",
            description="Test Description",
            price=500.0,
            quantity=10,
            country="Test Country",
            germination_period=14,
            color="Green"
        )

        assert grass.name == "Test Grass"
        assert grass.price == 500.0
        assert grass.quantity == 10
        assert grass.country == "Test Country"
        assert grass.germination_period == 14
        assert grass.color == "Green"

    def test_lawn_grass_inheritance(self):
        """Тест что LawnGrass наследуется от Product."""
        grass = LawnGrass("Grass", "Desc", 500.0, 10, "Country", 14, "Green")

        assert isinstance(grass, Product)
        assert issubclass(LawnGrass, Product)

    def test_lawn_grass_addition(self):
        """Тест сложения травы газонной."""
        grass1 = LawnGrass("Grass1", "Desc1", 500.0, 5, "Country1", 14, "Green")
        grass2 = LawnGrass("Grass2", "Desc2", 600.0, 3, "Country2", 10, "Dark Green")

        total_cost = grass1 + grass2
        expected_cost = (500.0 * 5) + (600.0 * 3)

        assert total_cost == expected_cost

    def test_str_representation(self):
        """Тест строкового представления LawnGrass."""
        grass = LawnGrass("Grass", "Desc", 500.0, 10, "Country", 14, "Green")
        expected = "Grass, 500.0 руб. Остаток: 10 шт. Страна: Country, Прорастание: 14 дней"
        assert str(grass) == expected
