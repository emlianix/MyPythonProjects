num = input()
letters = "АВЕКМНОРСТУХ"

# Проверяем общую длину номера: 2 цифры региона или 3 цифры региона
if (
    9 <= len(num) <= 10
    and num[0] in letters
    and num[1:4].isdigit()
    and num[4] in letters
    and num[5] in letters
    and num[6] == "_"
    and num[7:].isdigit()
):
    print("YES")
else:
    print("NO")