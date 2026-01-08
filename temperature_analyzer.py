"""
temperature_analyzer

This script analyzes patient body temperature and classifies health status
based on age-dependent thresholds.

Requirements implemented:
1. Accepts temperature in Celsius or Fahrenheit
2. Converts temperature to Celsius if needed
3. Classifies patient status based on temperature and age
4. Supports optional logging and displaying of results
"""
 
last_status = None
tmp_cache = None
debug_enabled = False

LOW_FEVER_THRESHOLD = 38
HIGH_FEVER_THRESHOLD = 39.4
BABY_FEVER_THRESHOLD = 37.4
HYPOTHERMIA_THRESHOLD = 30.0


def convert_to_celsius(temp_f):
    """
    Converts Fahrenheit to Celsius.

    Parameters:
        temp_f (float): temperature in Fahrenheit

    Returns:
        float: temperature in Celsius
    """

    if not isinstance(temp_f, (int, float)):
        raise TypeError("Temperature must be numeric")

    if temp_f < -100 or temp_f > 300:
        raise ValueError("Unrealistic temperature value")

    return (temp_f - 32) * 5 / 9


def has_fever(temp_c):
    """
    Determines if fever is present based on Celsius temperature.
    """
    if not isinstance(temp_c, (int, float)):
        raise TypeError("Temperature must be numeric")

    return temp_c > LOW_FEVER_THRESHOLD


def analyze_patient(temp, age, scale="C", verbose=False, emergency_mode=False, log=False):
    
    """
    Analyzes patient temperature and returns health status.

    Parameters:
        temp (float): temperature value
        age (int): patient age in years
        scale (str): 'C' or 'F'
        verbose (bool): enable console output
        emergency_mode (bool): enables hypothermia check
        log (bool): enable logging to file

    Returns:
        str: patient status
    """
    global last_status, tmp_cache
    
    if not isinstance(age, (int, float)) or age < 0:
        raise ValueError("Invalid age value")

    if not isinstance(temp, (int, float)):
        raise TypeError("Temperature must be numeric")

    if scale.upper() == "F":
        temp_c = convert_to_celsius(temp)
    elif scale.upper() == "C":
        temp_c = temp
    else:
        raise ValueError("Scale must be 'C' or 'F'")

    tmp_cache = temp_c

    if emergency_mode and temp_c < HYPOTHERMIA_THRESHOLD:
        last_status = "POSSIBLE HYPOTHERMIA"
        return last_status

    threshold = BABY_FEVER_THRESHOLD if age < 3 else HIGH_FEVER_THRESHOLD

    if temp_c > threshold:
        status = "FEVER"
    else:
        status = "NORMAL"

    last_status = status

    if verbose:
        print(f"Patient status: {status}")

    if log:
        try:
            with open("temp_log.txt", "a") as f:
                f.write(f"TEMP={temp_c}, AGE={age}, STATUS={status}\n")
        except IOError as e:
            print("Logging failed:", e)

    return status


def get_status_report(include_temp=False, format="long"):
    """
    Returns a formatted status report.
    """
    global last_status, tmp_cache

    if include_temp:
        return {"status": last_status, "temp_celsius": tmp_cache}
    elif format == "code":
        return last_status[:2] if last_status else None
    else:
        return f"Current status: {last_status}"


if __name__ == "__main__":

    temp = 109.7
    scale = "F"   # temperature unit explicitly defined
    age = 5

    print("Analyzing temperature:", temp, scale)

    result = analyze_patient(
        temp,
        age,
        scale=scale,
        verbose=True,
        emergency_mode=False,
        log=True
    )

    print("Result:", result)
    print("Last status:", last_status)
    print("Status report:", get_status_report(include_temp=True))
