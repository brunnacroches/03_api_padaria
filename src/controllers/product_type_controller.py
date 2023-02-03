from models.models import Product

class ProductTypeController:
    def get_products_by_type(type):
        if type not in ["Bolo", "Doce", "Salgado"]:
            raise ValueError("Invalid product type")

        products = Product.search_by_type(type)
        return [{'name': p.name, 'price': p.price} for p in products]


