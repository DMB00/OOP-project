import pytest
from src.models import Product, Category


class TestProduct:
    """Тесты для класса Product."""

    def test_product_initialization(self):
        """Тест корректности инициализации объекта Product."""
        product = Product(
            name="Test Product",
            description="Test Description",
            price=1000.0,
            quantity=5
        )

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 5

    def test_product_attributes_types(self):
        """Тест типов атрибутов Product."""
        product = Product("Test", "Desc", 999.99, 10)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест корректности инициализации объекта Category."""
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
        assert category.products == products
        assert len(category.products) == 2

    def test_category_count_increment(self):
        """Тест подсчета количества категорий."""
        initial_count = Category.category_count

        product = Product("P1", "D1", 100.0, 1)
        category1 = Category("Cat1", "Desc1", [product])
        category2 = Category("Cat2", "Desc2", [product])

        assert Category.category_count == initial_count + 2
        assert category1.category_count == 2
        assert category2.category_count == 2

    def test_product_count_increment(self):
        """Тест подсчета количества товаров."""
        initial_product_count = Category.product_count

        product1 = Product("P1", "D1", 100.0, 1)
        product2 = Product("P2", "D2", 200.0, 2)
        product3 = Product("P3", "D3", 300.0, 3)

        category1 = Category("Cat1", "Desc1", [product1, product2])
        category2 = Category("Cat2", "Desc2", [product3])

        total_products = len(category1.products) + len(category2.products)
        assert Category.product_count == initial_product_count + total_products
        assert Category.product_count == 3

    def test_empty_category(self):
        """Тест создания категории без товаров."""
        category = Category("Empty Category", "No products", [])

        assert category.name == "Empty Category"
        assert category.description == "No products"
        assert category.products == []
        assert len(category.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_with_single_product(self):
        """Тест создания категории с одним товаром."""
        product = Product("Single", "Single product", 500.0, 1)
        category = Category("Single Category", "One product", [product])

        assert len(category.products) == 1
        assert category.products[0].name == "Single"
        assert Category.product_count == 1

    @pytest.fixture
    def sample_products(self):
        """Фикстура для создания тестовых товаров."""
        return [
            Product("Phone", "Smartphone", 1000.0, 5),
            Product("Tablet", "Tablet device", 800.0, 3),
            Product("Laptop", "Laptop computer", 1500.0, 2)
        ]

    def test_category_with_fixture(self, sample_products):
        """Тест категории с использованием фикстуры."""
        category = Category("Electronics", "Electronic devices", sample_products)

        assert category.name == "Electronics"
        assert len(category.products) == 3
        assert Category.product_count == 3
