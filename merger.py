def merge_lists(*args) -> list:
    """Объединяет произвольное количество списков в один."""
    result = []
    for lst in args:
        result.extend(lst)
    return result