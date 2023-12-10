from decimal import Decimal

from flask import jsonify, abort, Blueprint
from werkzeug.exceptions import BadRequest

from cars_manager_app.cars.enums import Sort, Statistics
from cars_manager_app.web.security import token_required
from ..configuration import load_cars_service

service = load_cars_service()

cars_grouped_bp = Blueprint('cars/grouped', __name__)
most_expensive_bp = Blueprint('cars/most/expensive', __name__)


def create_routing(app):
    """
    -> /cars
        -> /grouped
            -> /price
            -> /mileage_range
            -> /mileage_threshold
            -> /given_param
            -> /components
        -> /most/expensive
            -> /
            -> /model
        -> /counted
            -> /color
        -> /sort
            -> /components
        -> /statistics
    """


    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return jsonify({'error': 'Invalid request parameters'}), 400

    @cars_grouped_bp.route('/given_param/<string:param>-<string:desc>')
    @token_required
    def sort(param: str, desc: str):
        param = param.upper()
        desc_bool = bool(desc)

        if param not in Sort.__members__:
            abort(400, description='Invalid sort value')

        return jsonify(service.sort(service.get_comparison_func(Sort[param]), desc_bool))

    @cars_grouped_bp.route('/mileage_threshold/<int:max_mileage>')
    @token_required
    def get_cars_with_mileage_greater_than(max_mileage: int):
        return jsonify(service.get_cars_with_mileage_greater_than(max_mileage))

    @app.route('/cars/counted/color')
    @token_required
    def count_cars_with_color():
        return jsonify(service.count_cars_with_color())

    @most_expensive_bp.route('/models')
    @token_required
    def get_most_expensive_cars_per_model():
        return jsonify(service.get_most_expensive_cars_per_model())

    @app.route('/cars/statistics/<string:stat>')
    @token_required
    def get_car_statistics(stat: str):

        if stat not in [member.value for member in Statistics]:
            abort(400, description='Wrong statistics type value')

        return jsonify(service.get_car_statistics(Statistics(stat)))

    @app.route('/cars/sort/components')
    @token_required
    def get_cars_with_sorted_components():
        return jsonify(service.get_cars_with_sorted_components())

    @cars_grouped_bp.route('/price/<string:min_value>-<string:max_value>')
    @token_required
    def get_cars_with_price_within_range(min_value: str, max_value: str):
        decimal_min_val, decimal_max_val = Decimal(min_value), Decimal(max_value)

        if decimal_min_val > decimal_max_val:
            abort(400, description='Min value cannot be greater than max value')
        return jsonify(service.get_cars_with_price_within_range(decimal_min_val, decimal_max_val))

    @most_expensive_bp.route('/')
    @token_required
    def get_most_expensive():
        return jsonify(service.get_most_expensive())

    @cars_grouped_bp.route('/components')
    @token_required
    def get_cars_per_components():
        return jsonify(service.get_cars_per_components())
