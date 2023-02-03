from controllers.product_type_controller import ProductTypeController


class ActionViewProductType:
    def view_products_type(self, request):
        body = request.json
        type = body.type

        action_controller_products_type = ProductTypeController()
        action_controller_products_type.get_products_by_type(type)

        return {
            "status_code": 200,
            "data": {
                "type": type,
            },
            "success": True
        }