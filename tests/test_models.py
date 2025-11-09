import pytest
from src.models import Product, Category


class TestProduct:
    """Тесты для класса Product."""

    def test_old_functionality_initialization(self):
        """Тест СТАРОЙ функциональности - инициализации объекта Product."""
        product = Product(
            name="Test Product",
            description="Test Description",
            price=1000.0,
            quantity=5
        )

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0  # Теперь через property
        assert product.quantity == 5

    def test_old_functionality_attributes_types(self):
        """Тест СТАРОЙ функциональности - типов атрибутов Product."""
        product = Product("Test", "Desc", 999.99, 10)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)  # Теперь через property
        assert isinstance(product.quantity, int)

    def test_new_functionality_price_getter(self):
        """Тест НОВОЙ функциональности - геттера цены."""
        product = Product("Test", "Desc", 150.0, 1)
        assert product.price == 150.0

    def test_new_functionality_price_setter_negative(self, capsys):
        """Тест НОВОЙ функциональности - сеттера цены с отрицательным значением."""
        product = Product("Test", "Desc", 100.0, 1)
        product.price = -50
        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не изменилась

    def test_new_functionality_price_setter_zero(self, capsys):
        """Тест НОВОЙ функциональности - сеттера цены с нулевым значением."""
        product = Product("Test", "Desc", 100.0, 1)
        product.price = 0
        captured = capsys.readouterr()

        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не изменилась

    def test_new_functionality_price_setter_positive(self):
        """Тест НОВОЙ функциональности - сеттера цены с положительным значением."""
        product = Product("Test", "Desc", 100.0, 1)
        product.price = 150.0
        assert product.price == 150.0

    def test_new_functionality_new_product_class_method(self):
        """Тест НОВОЙ функциональности - класс-метода new_product."""
        product_data = {
            'name': 'New Product',
            'description': 'New Description',
            'price': 500.0,
            'quantity': 10
        }

        product = Product.new_product(product_data)

        assert product.name == 'New Product'
        assert product.description == 'New Description'
        assert product.price == 500.0
        assert product.quantity == 10


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_old_functionality_initialization(self):
        """Тест СТАРОЙ функциональности - инициализации объекта Category."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        products = [product1, product2]

        category = Category(
            name="Test Category",
            description="Test Category Description",
            products=products
        )

        assert category.name == "Test Category"
        assert category.description == "Test Category Description"
        assert len(category.products) == 2  # Теперь через property

    def test_old_functionality_category_count_increment(self):
        """Тест СТАРОЙ функциональности - подсчета количества категорий."""
        initial_count = Category.category_count

        product = Product("P1", "D1", 100.0, 1)
        category1 = Category("Cat1", "Desc1", [product])
        category2 = Category("Cat2", "Desc2", [product])

        assert Category.category_count == initial_count + 2
        assert category1.current_category_count == 2  # Старое свойство
        assert category2.current_category_count == 2  # Старое свойство

    def test_old_functionality_product_count_increment(self):
        """Тест СТАРОЙ функциональности - подсчета количества товаров."""
        initial_product_count = Category.product_count

        product1 = Product("P1", "D1", 100.0, 1)
        product2 = Product("P2", "D2", 200.0, 2)
        product3 = Product("P3", "D3", 300.0, 3)

        category1 = Category("Cat1", "Desc1", [product1, product2])
        category2 = Category("Cat2", "Desc2", [product3])

        assert Category.product_count == initial_product_count + 3
        assert Category.product_count == 3

    def test_new_functionality_private_products_attribute(self):
        """Тест НОВОЙ функциональности - приватности атрибута products."""
        product = Product("Test", "Desc", 100.0, 1)
        category = Category("Test", "Desc", [product])

        # Проверяем что нельзя получить доступ напрямую к __products
        with pytest.raises(AttributeError):
            _ = category.__products

    def test_new_functionality_add_product_method(self):
        """Тест НОВОЙ функциональности - метода add_product."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        category = Category("Test", "Desc", [product1])

        initial_count = Category.product_count

        product2 = Product("Product2", "Desc2", 200.0, 3)
        category.add_product(product2)

        assert len(category.products) == 2
        assert Category.product_count == initial_count + 1  # +1 к счетчику

    def test_new_functionality_products_property_format(self):
        """Тест НОВОЙ функциональности - геттера products с правильным форматом."""
        product = Product("Test Product", "Test Desc", 150.0, 5)
        category = Category("Test", "Desc", [product])

        products_info = category.products
        expected_format = "Test Product, 150.0 руб. Остаток: 5 шт."

        assert len(products_info) == 1
        assert products_info[0] == expected_format

    def test_old_functionality_empty_category(self):
        """Тест СТАРОЙ функциональности - создания категории без товаров."""
        category = Category("Empty Category", "No products", [])

        assert category.name == "Empty Category"
        assert category.description == "No products"
        assert len(category.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    @pytest.fixture
    def sample_category(self):
        """Фикстура для создания тестовой категории."""
        products = [
            Product("Phone", "Smartphone", 1000.0, 5),
            Product("Tablet", "Tablet device", 800.0, 3)
        ]
        return Category("Electronics", "Electronic devices", products)

    def test_mixed_functionality_with_fixture(self, sample_category):
        """Тест смешанной функциональности с использованием фикстуры."""
        # Старая функциональность
        assert sample_category.name == "Electronics"
        assert Category.category_count == 1

        # Новая функциональность
        assert len(sample_category.products) == 2
        assert "Phone, 1000.0 руб. Остаток: 5 шт." in sample_category.products
