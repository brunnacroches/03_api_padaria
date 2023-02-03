import unittest
from product_type_controller import ProductTypeController

class TestProductTypeController(unittest.TestCase):
    def test_get_products_by_type_success(self):
        # Given
        type = "Bolo"

        # When
        result = ProductTypeController.get_products_by_type(type)

        # Then
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        for product in result:
            self.assertIn("name", product)
            self.assertIn("price", product)

    def test_get_products_by_type_success_2(self):
        # Given
        type = "Doce"

        # When
        result = ProductTypeController.get_products_by_type(type)

        # Then
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

        for product in result:
            self.assertIn("name", product)
            self.assertIn("price", product)
        
    def test_get_products_by_type_value_error(self):
        # Given
        type = "Invalid"

        # When
        with self.assertRaises(ValueError):
            result = ProductTypeController.get_products_by_type(type)

    def test_get_products_by_type_value_error_2(self):
        # Given
        type = "Other Invalid"

        # When
        with self.assertRaises(ValueError):
            result = ProductTypeController.get_products_by_type(type)
