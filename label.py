def label(colors):
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    if len(colors) < 3 or len(colors) > 4:
        return ""

    first_digit = color_map[colors[0]]
    second_digit = color_map[colors[1]]
    multiplier = 10 ** color_map[colors[2]]

    resistance_value = (first_digit * 10 + second_digit) * multiplier

    if resistance_value >= 1_000_000_000:
        value_str = f"{resistance_value / 1_000_000_000:.1f}".rstrip('0').rstrip('.') + " gigaohms"
    elif resistance_value >= 1_000_000:
        value_str = f"{resistance_value / 1_000_000:.1f}".rstrip('0').rstrip('.') + " megaohms"
    elif resistance_value >= 1_000:
        value_str = f"{resistance_value / 1_000:.1f}".rstrip('0').rstrip('.') + " kiloohms"
    else:
        value_str = f"{resistance_value} ohms"

    return value_str
