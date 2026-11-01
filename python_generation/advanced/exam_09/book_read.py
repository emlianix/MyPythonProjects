m = int(input())
n = int(input())
# Считываем книги домашней библиотеки в множество для быстрого поиска
library = {input() for _ in range(m)}

# Проверяем книги из списка на лето
for _ in range(n):
  book = input()
  if book in library:
    print("YES")
  else:
    print("NO")