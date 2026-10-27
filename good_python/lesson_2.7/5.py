rect_width, rect_height, w, h = map(int, input().split())

# Находим общее количество прямоугольников
# bool(rect_width % w) даст True (1), если есть остаток, и False (0), если остатка нет
cols = rect_width // w + bool(rect_width % w)
rows = rect_height // h + bool(rect_height % h)

# Общее количество покрываемых сеткой прямоугольников
total_rects = cols * rows
# Количество прямоугольников, которые поместились
fitted_rects = (rect_width // w) * (rect_height // h)
# Количество не поместившихся целиком прямоугольников
total = total_rects - fitted_rects