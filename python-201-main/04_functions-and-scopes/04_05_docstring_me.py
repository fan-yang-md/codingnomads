# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """_summary_

    Args:
        km (float): distance in km

    Returns:
        float: distance in km
    """

    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
