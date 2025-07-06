def split_names_ages(data: list[tuple]) -> tuple[list, list]:
    """Разделяет список кортежей (имя, возраст) на два списка."""
    names, ages = [], []
    for name, age in data:
        names.append(name)
        ages.append(age)
    return names, ages