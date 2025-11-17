import pytest
from src.models import Product, Category, Smartphone, LawnGrass, CategoryIterator


class TestProduct:
    """Тесты для базового класса Product."""

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


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.category_count = 0
        Category.product_count = 0

    def test_add_product_validation(self):
        """Тест валидации при добавлении продукта."""
        category = Category("Test", "Desc", [])

        # Корректное добавление Product
        product = Product("Product", "Desc", 100.0, 2)
        category.add_product(product)
        assert len(category.products_list) == 1

        # Корректное добавление Smartphone (наследник Product)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 4.5, "Model", 128, "Black")
        category.add_product(smartphone)
        assert len(category.products_list) == 2

        # Корректное добавление LawnGrass (наследник Product)
        grass = LawnGrass("Grass", "Desc", 500.0, 5, "Country", 14, "Green")
        category.add_product(grass)
        assert len(category.products_list) == 3

    def test_add_product_invalid_type(self):
        """Тест добавления невалидного типа в категорию."""
        category = Category("Test", "Desc", [])

        with pytest.raises(TypeError):
            category.add_product("invalid product")

        with pytest.raises(TypeError):
            category.add_product(123)

        with pytest.raises(TypeError):
            category.add_product(None)

    def test_mixed_products_in_category(self):
        """Тест работы категории со смешанными типами продуктов."""
        product = Product("Product", "Desc", 100.0, 2)
        smartphone = Smartphone("Phone", "Desc", 1000.0, 2, 4.5, "Model", 128, "Black")
        grass = LawnGrass("Grass", "Desc", 500.0, 5, "Country", 14, "Green")

        category = Category("Mixed", "Description", [product, smartphone, grass])

        assert len(category.products_list) == 3
        assert isinstance(category.products_list[0], Product)
        assert isinstance(category.products_list[1], Smartphone)
        assert isinstance(category.products_list[2], LawnGrass)

    def test_old_functionality_preserved(self):
        """Тест что старая функциональность категории сохранена."""
        product = Product("Product", "Desc", 100.0, 2)
        category = Category("Test", "Desc", [product])

        assert category.name == "Test"
        assert len(category.products_list) == 1
        assert Category.category_count == 1

    def test_str_representation(self):
        """Тест строкового представления Category."""
        product = Product("Product", "Desc", 100.0, 3)
        category = Category("Test", "Desc", [product])
        expected = "Test, количество продуктов: 3 шт."
        assert str(category) == expected

    def test_str_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Test", "Desc", [])
        expected = "Test, количество продуктов: 0 шт."
        assert str(category) == expected

    def test_len(self):
        """Тест метода __len__ категории."""
        product1 = Product("P1", "D1", 100.0, 2)
        product2 = Product("P2", "D2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])
        assert len(category) == 2

    def test_iteration(self):
        """Тест итерации по категории."""
        product1 = Product("P1", "D1", 100.0, 2)
        product2 = Product("P2", "D2", 200.0, 3)
        category = Category("Test", "Desc", [product1, product2])

        products = list(category)
        assert len(products) == 2
        assert products[0] == product1
        assert products[1] == product2


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

        collected_products = []
        for product in CategoryIterator([product1, product2]):
            collected_products.append(product)

        assert collected_products == [product1, product2]
