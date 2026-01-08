def CheckHydration(weight_kg, height_m, activity_level="mid"):
    """
    Computes daily hydration needs for a patient.

    Parameters:
        weight_kg (float): body weight in kilograms
        height_m (float): height in meters
        activity_level (str): "low", "mid", or "high"

    Returns:
        float: daily hydration requirement in liters

    Notes:
        - Does not account for fever or hot climate
        - For demo purposes only, not for clinical use
    """

    if not isinstance(weight_kg, (int, float)) or weight_kg <= 0:
        raise ValueError("Weight must be a positive number")

    if not isinstance(height_m, (int, float)) or height_m <= 0:
        raise ValueError("Height must be a positive number")

    if not isinstance(activity_level, str):
        raise ValueError("Activity level must be a string")

    activity_level = activity_level.lower()

    if activity_level not in ["low", "mid", "high"]:
        raise ValueError("Activity level must be 'low', 'mid', or 'high'")

    base_liters = 30 * weight_kg / 1000

    if activity_level == "low":
        factor = 0.9
    elif activity_level == "mid":
        factor = 1.0
    else:  # high
        factor = 1.2

    daily_liters = base_liters * factor

    return round(daily_liters, 2)
