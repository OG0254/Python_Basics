def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5.0 / 9.0


print(convert_to_celsius(100))  # Output: 37.77777777777778
