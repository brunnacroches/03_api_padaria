

class ProductSearchController:
    def __init__(self, product_controller):
        self.products = product_controller.products
    
    def search_products_by_type(self, type):
        if type not in ["Bolo", "Doce", "Salgado"]:
            raise ValueError("Tipo inválido. Os tipos permitidos são: Bolo, Doce, Salgado")
        return [product for product in self.products if product["type"] == type]
