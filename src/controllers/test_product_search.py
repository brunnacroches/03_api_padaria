import unittest
from products_controller import ProductsController
from product_search_controller import ProductSearchController

class TestProductSearchController(unittest.TestCase):
    def setUp(self):
        self.products_controller = ProductsController()
        self.product_search_controller = ProductSearchController(self.products_controller)

        self.products_controller.create_product("Bolo de chocolate", 20.0, "Bolo")
        self.products_controller.create_product("Bolo de morango", 22.0, "Bolo")
        self.products_controller.create_product("Doce de leite", 10.0, "Doce")
        self.products_controller.create_product("Pastel de carne", 8.0, "Salgado")

    def test_search_products_by_type_valid_input(self):
        result = self.product_search_controller.search_products_by_type("Bolo")
        expected_result = [{"name": "Bolo de chocolate", "price": 20.0, "type": "Bolo"},
                           {"name": "Bolo de morango", "price": 22.0, "type": "Bolo"}]
        self.assertEqual(result, expected_result)

    def test_search_products_by_type_invalid_input(self):
        with self.assertRaises(ValueError):
            result = self.product_search_controller.search_products_by_type("InvalidType")

    # Adicione mais dois testes de acordo com sua necessidade
