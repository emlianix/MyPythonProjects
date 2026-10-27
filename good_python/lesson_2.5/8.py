from math import sqrt, acos, pi

x0, y0, x1, y1 = map(float, input().split())

cos_a = (x0 * x1 + y0 * y1) / (sqrt(x0**2 + y0**2) * sqrt(x1**2 + y1**2))
a = acos(cos_a)
# Переводим в градусы
grad_a = (180 / pi) * a
# Округляем до десятых и записываем в переменную alpha
alpha = round(grad_a, 1)