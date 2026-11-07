length_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.344,
}
weight_units = {"mg": 0.001, "g": 1, "kg": 1000, "oz": 28.349523125, "lb": 453.59237}


def convert_length(value, from_unit, to_unit):
    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("this unit is unknown")

    from_factor = length_units[from_unit]
    to_factor = length_units[to_unit]
    result = (value * from_factor) / to_factor
    return result


def convert_weight(value, from_unit, to_unit):
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("this unit is unknown")

    from_factor = weight_units[from_unit]
    to_factor = weight_units[to_unit]
    result = (value * from_factor) / to_factor
    return result
