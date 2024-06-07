from label import label


def test_label():
    test_cases = [
        (["orange", "orange", "black"], "33 ohms"),
        (["blue", "grey", "brown"], "680 ohms"),
        (["red", "violet", "yellow"], "270 kiloohms"),
        (["green", "blue", "red"], "5.6 kiloohms"),
        (["brown", "black", "orange"], "10 kiloohms"),
        (["blue", "green", "yellow"], "650 kiloohms"),
        (["blue", "green", "yellow", "orange"], "650 kiloohms"),
        (["white", "white", "white"], "99 gigaohms")
    ]

    for colors, expected in test_cases:
        result = label(colors)
        assert result == expected, f"Expected '{expected}', but got '{result}'"

    print("All tests passed!")
