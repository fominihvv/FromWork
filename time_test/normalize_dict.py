def normalize_dict(nested_dict: dict) -> dict:
    total = []
    for value in nested_lists:
        if isinstance(value, int):
            total.append(value)
        if isinstance(value, list):
            total += linear(value)
    return total


