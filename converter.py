units_dict = {"mm":0.001, "cm":0.01, "m":1, "km":1000}

def convert_length(value,from_unit,to_unit):
    if from_unit not in units_dict or to_unit not in units_dict:
        raise ValueError("this unit is unknown")

    from_factor = units_dict[from_unit]
    to_factor = units_dict[to_unit]
    result = (value * from_factor) / to_factor
    return result


    
    
