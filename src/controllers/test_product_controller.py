import unittest
from products_controller import ProductsController

class TestProductsController(unittest.TestCase):
    def setUp(self):
        self.products_controller = ProductsController()

    def test_create_product_valid_input(self):
        result = self.products_controller.create_product("Bolo de chocolate", 20.0, "Bolo")
        self.assertEqual(result, 'Produto cadastrado com sucesso')

    def test_create_product_invalid_input(self):
        with self.assertRaises(ValueError):
            result = self.products_controller.create_product("Bolo de chocolate", 20.0, "InvalidType")

    # Adicione mais dois testes de acordo com sua necessidade
