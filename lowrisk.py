# lowrisk.py

def calculate_average(values):
    """
    Safely calculates average of a list.
    Does not affect existing system.
    """
    if not values:
        return 0

    return sum(values) / len(values)


def greet_user(name):
    return f"Hello, {name}!"