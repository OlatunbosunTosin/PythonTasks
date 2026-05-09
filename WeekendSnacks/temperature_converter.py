def converter(temperature):
    converted_temperature = 0.0

    if temperature[-1].lower() == "c":
        converted_temperature = (float(temperature[:-1]) * (1.8)) + 32

    elif temperature[-1].lower() == "f":
        converted_temperature = (float(temperature[:-1]) - 32) * (5/9)

    else:
        converted_temperature = (float(temperature) * 1.8) + 32

    return converted_temperature


def advisary_message(temperature, threshold_value):
    converted_value = converter(temperature)

    if converted_value < threshold_value:
        return "Cold advisory"
    else:
        return "Heat alert"
