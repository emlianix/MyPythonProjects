text = input()
eng = "eyopaxcETOPAHXCBM"
rus = "еуорахсЕТОРАНХСВМ"

old_cost = 0
for char in text:
    old_cost += ord(char) * 3

new_text = text
for i in range(len(eng)):
    new_text = new_text.replace(eng[i], rus[i])

new_cost = 0
for char in new_text:
    new_cost += ord(char) * 3

print(f"Старая стоимость: {old_cost}🐝")
print(f"Новая стоимость: {new_cost}🐝")