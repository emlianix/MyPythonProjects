shown = {int(x) for x in input().split()}
answers = {int(x) for x in input().split()}

# Сравниваем множества: если они полностью совпадают, то кандидат прошёл тест
if shown == answers:
  print("YES")
else:
  print("NO")