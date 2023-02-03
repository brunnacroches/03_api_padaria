from controllers.product_search_controller import ProductSearchController

class ActionViewProductSearch:
    def view_products_search(self, request):
        body = request.json
        type = body.type

        action_controller_products_search = ProductSearchController()
        action_controller_products_search.search_products_by_type(type)

        return {
            "status_code": 200,
            "data": {
                "type": type,
            },
            "success": True
        }