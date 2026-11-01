def is_subfolder(folder_dict, subfolder, folder):
    stack = list(folder_dict.get(folder, []))
    visited = set()

    while stack:
        current = stack.pop()
        if current == subfolder:
            return True
        if current in visited:
            continue
        visited.add(current)
        stack.extend(folder_dict.get(current, []))

    return False