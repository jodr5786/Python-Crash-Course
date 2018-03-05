def make_car(manufacturer, model_name, **optional_features):
    """Build a dictionary about a car."""
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name
    for key, value in optional_features.items():
        car_info[key] = value
    return car_info

car = make_car ('Ford', 
                'F150',
                towing_package = 'yes',
                engine = 'ecoboost',
                sport_package = 'yes',)

print(car)


