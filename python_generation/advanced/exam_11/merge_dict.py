def merge(values):
    result = {}
    for d in values:
        for key, value in d.items():
            result.setdefault(key, set()).add(value)
    return result