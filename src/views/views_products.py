from controllers.products_controller import ProductsController

class ActionViewProducts:
    def view_products(self, request):
        body = request.json
        name = body.name
        type = body.type
        price = body.price

        action_controller_products = ProductsController()
        action_controller_products.create_product(name, type, price)

        return {
            "status_code": 200,
            "data": {
                "price": price,
                "type": type,
                "name": name
            },
            "success": True
        }