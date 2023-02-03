from models.models import Product


class ProductsController:
    def __init__(self):
        self.products = []

    def create_product(self, name, price, type):
        if type not in ["Bolo", "Doce", "Salgado"]:
            raise ValueError("Tipo inválido. Os tipos permitidos são: Bolo, Doce, Salgado")
        self.products.append({"name": name, "price": price, "type": type})

        products = Product(name, price, type)
        products.salve()
        return 'Produto cadastrado com sucesso'

