import random

empty_teapot_weight = 117
cap_weight = 25
water_min_weight = 70
water_max_weight = 90
leaves_min_weight = 4
leaves_max_weight = 30
tolerance = 10

empty_threshold = 3


def noise(level=tolerance):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            noise_value = (random.random() * level / 200) * random.choice([-1, 1])
            return result + noise_value

        return wrapper

    return decorator


@noise(level=empty_threshold)
def empty():
    return 0


@noise()
def empty_teapot():
    return empty() + empty_teapot_weight + leaves_min_weight


@noise()
def full_teapot():
    return empty_teapot() + water_max_weight + cap_weight


@noise()
def full_teapot_cap():
    return empty_teapot() + leaves_max_weight + water_max_weight + cap_weight + tolerance


def identify_teapot_state(weight):
    # Порог для определения, что весы пусты (например, вес меньше 1 грамма)
    empty_threshold = 3

    # Диапазоны весов для различных состояний
    states = {
        "empty": (
            -empty_threshold,
            empty_threshold
        ),
        "teapot": (
            empty_teapot_weight - tolerance,
            empty_teapot_weight + tolerance
        ),
        "teapot+leaves": (
            empty_teapot_weight + leaves_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + tolerance
        ),
        "teapot+leaves+cap": (
            empty_teapot_weight + leaves_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + cap_weight + tolerance
        ),
        "teapot+leaves+water": (
            empty_teapot_weight + leaves_min_weight + water_min_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + tolerance
        ),
        "teapot+leaves+water+cap": (
            empty_teapot_weight + leaves_min_weight + water_min_weight + cap_weight - tolerance,
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance
        ),
        "teapot+leaves+water+cap+unknown": (
            empty_teapot_weight + leaves_max_weight + water_max_weight + cap_weight + tolerance,
            300
        ),
    }

    for state, (min_weight, max_weight) in states.items():
        if min_weight <= weight <= max_weight:
            state_sets = set(state.split('+'))
            return state_sets

    return "not_teapot"
