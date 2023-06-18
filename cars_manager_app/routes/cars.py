from flask import jsonify
from decimal import Decimal

from ..app import main
from cars_manager_app.cars.enums import Sort, Statistics

service = main()


def create_routing(app):
    """
    -> /cars
        -> /grouped
            -> /by_price
            -> /by_mileage_range
            -> /by_mileage_threshold
            -> /by_given_param
            -> /by_components
        -> /most
            -> /expensive
            -> /expensive_models
        -> /counted
            -> color
        -> /with
            -> /sorted_components
        -> /spec_stats
            
    """

    @app.route('/cars/grouped/by_given_param/<string:param>-<string:desc>')
    def sort(param: str, desc: str):
        param = param.upper()
        desc_bool = bool(desc)

        if param not in Sort.__members__:
            return jsonify({'message': 'Invalid sort value'})

        return jsonify(service.sort(Sort[param], desc_bool))

    @app.route('/cars/grouped/by_mileage_threshold/<int:max_mileage>')
    def get_cars_with_mileage_greater_than(max_mileage: int):
        return jsonify(service.get_cars_with_mileage_greater_than(max_mileage))

    @app.route('/cars/counted/color')
    def count_cars_with_color():
        return jsonify(service.count_cars_with_color())

    @app.route('/cars/most/expensive_models')
    def get_most_expensive_cars_per_model():
        return jsonify(service.get_most_expensive_cars_per_model())

    @app.route('/cars/spec_stats/<string:stat>')
    def get_car_statistics(stat: str):
        if stat in [member.value for member in Statistics]:
            return jsonify(service.get_car_statistics(Statistics(stat)))

        return jsonify({'message': 'Invalid statistics parameter'})

    @app.route('/cars/with/sorted_components')
    def get_cars_with_sorted_components():
        return jsonify(service.get_cars_with_sorted_components())

    @app.route('/cars/grouped/by_price/<string:min_value>-<string:max_value>')
    def get_cars_with_price_within_range(min_value: str, max_value: str):
        decimal_min_val, decimal_max_val = Decimal(min_value), Decimal(max_value)

        if decimal_min_val > decimal_max_val:
            return jsonify({'message': "Wrong parameters"})

        return jsonify(service.get_cars_with_price_within_range(decimal_min_val, decimal_max_val))

    @app.route('/cars/most/expensive')
    def get_most_expensive():
        return jsonify(service.get_most_expensive())

    @app.route('/cars/grouped/by_components')
    def get_cars_per_components():
        return jsonify(service.get_cars_per_components())


