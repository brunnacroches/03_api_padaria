from flask import jsonify, request
from views.views_products import ActionViewProducts
from views.views_search_controller import ActionViewProductSearch
from views.views_type_products import ActionViewProductType

from .server import app

# ? POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/products", methods=["POST"])
def route_products():
    action_view_products = ActionViewProducts()

    http_response = action_view_products.view_products(request)

    return jsonify(http_response["data"]), http_response["status_code"]

# ? POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/serach", methods=["POST"])
def route_search_products():
    action_view_search_products = ActionViewProductSearch()

    http_response = action_view_search_products.view_products_search(request)

    return jsonify(http_response["data"]), http_response["status_code"]

# ? POST PARA CRIAR UM NOVO RECURSO
@app.route("/rota1/typeproduct", methods=["POST"])
def route_type_product():
    action_view_tpye_product = ActionViewProductType()

    http_response = action_view_tpye_product.view_products_type(request)

    return jsonify(http_response["data"]), http_response["status_code"]
