def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """
    Calculate BMI for each pair of height and weight.

    Args:
        height (list[float]): List of heights in meters.
        weight (list[float]): List of weights in kilograms.

    Returns:
        list[float]: List of BMI values.

    Raises:
        ValueError: If input lists are not of the same length.
        TypeError: If inputs are not lists of numbers.
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("All height values must be integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("All weight values must be integers or floats.")
    if not all(h > 0 for h in height):
        raise ValueError("All height values must be greater than zero.")
    if not all(w > 0 for w in weight):
        raise ValueError("All weight values must be greater than zero.")

    bmi_list = [w / (h ** 2) for h, w in zip(height, weight)]
    return bmi_list


def apply_limit(bmi: list[float], limit: float) -> list[bool]:
    """
    Determine if each BMI value exceeds the given limit.

    Args:
        bmi (list[float]): List of BMI values.
        limit (float): The BMI limit to compare against.

    Returns:
        list[bool]: List indicating if each BMI exceeds the limit.

    Raises:
        TypeError: If inputs are not of the correct type.
    """
    if not isinstance(bmi, list):
        raise TypeError("BMI must be a list.")
    if not isinstance(limit, (int, float)):
        raise TypeError("Limit must be an integer or float.")
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("All BMI values must be integers or floats.")

    result = [b > limit for b in bmi]
    return result
