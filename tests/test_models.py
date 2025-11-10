import pytest
from src.models import Product, Category, CategoryIterator


class TestProduct:
    """Тесты для класса Product."""

    def test_str_representation(self):
        """Тест строкового представления продукта."""
        product = Product("Test Product", "Test Description", 1000.0, 5)
        expected_str = "Test Product, 1000.0 руб. Остаток: 5 шт."

        assert str(product) == expected_str

    def test_addition_products(self):
        """Тест сложения двух продуктов."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)

        total_cost = product1 + product2
        expected_cost = (100.0 * 2) + (200.0 * 3)

        assert total_cost == expected_cost

    def test_addition_multiple_products(self):
        """Тест сложения нескольких продуктов по отдельности."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        product3 = Product("Product3", "Desc3", 300.0, 1)

        # Складываем попарно
        cost1 = product1 + product2
        total_cost = cost1 + (product3.price * product3.quantity)
        expected_cost = (100.0 * 2) + (200.0 * 3) + (300.0 * 1)

        assert total_cost == expected_cost

    def test_addition_invalid_type(self):
        """Тест сложения с неверным типом."""
        product = Product("Test", "Desc", 100.0, 1)

        with pytest.raises(TypeError):
            _ = product + "invalid"

    def test_old_functionality_preserved(self):
        """Тест что старая функциональность сохранена."""
        product = Product("Test", "Desc", 150.0, 5)

        # Старые атрибуты доступны
        assert product.name == "Test"
        assert product.description == "Desc"
        assert product.price == 150.0
        assert product.quantity == 5


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_str_representation(self):
        """Тест строкового представления категории."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test Category", "Description", [product1, product2])

        expected_str = "Test Category, количество продуктов: 5 шт."
        assert str(category) == expected_str

    def test_str_empty_category(self):
        """Тест строкового представления пустой категории."""
        category = Category("Empty Category", "No products", [])

        expected_str = "Empty Category, количество продуктов: 0 шт."
        assert str(category) == expected_str

    def test_products_property_optimized(self):
        """Тест оптимизированного геттера products."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])

        products_info = category.products
        expected_info = "Product1, 100.0 руб. Остаток: 2 шт.\nProduct2, 200.0 руб. Остаток: 3 шт."

        assert products_info == expected_info

    def test_iteration(self):
        """Тест итерации по категории."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])

        products = list(category)
        assert len(products) == 2
        assert products[0] == product1
        assert products[1] == product2

    def test_old_functionality_preserved(self):
        """Тест что старая функциональность категории сохранена."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])

        # Старые методы работают
        assert category.name == "Test"
        assert len(category.products_list) == 2
        assert Category.category_count == 1


class TestCategoryIterator:
    """Тесты для класса CategoryIterator."""

    def test_iterator_initialization(self):
        """Тест инициализации итератора."""
        products = [
            Product("Product1", "Desc1", 100.0, 2),
            Product("Product2", "Desc2", 200.0, 3)
        ]
        iterator = CategoryIterator(products)

        assert iterator.products == products
        assert iterator.index == 0

    def test_iterator_next(self):
        """Тест метода next итератора."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        products = [product1, product2]
        iterator = CategoryIterator(products)

        assert next(iterator) == product1
        assert next(iterator) == product2

        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_for_loop(self):
        """Тест использования итератора в цикле for."""
        product1 = Product("Product1", "Desc1", 100.0, 2)
        product2 = Product("Product2", "Desc2", 200.0, 3)
        products = [product1, product2]

        collected_products = []
        for product in CategoryIterator(products):
            collected_products.append(product)

        assert collected_products == products