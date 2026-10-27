timur = input()
ruslan = input()

if timur == ruslan:
    print("ничья")

elif (timur == "камень" and (ruslan == "ножницы" or ruslan == "ящерица")):
    print("Тимур")

elif (timur == "ножницы" and (ruslan == "бумага" or ruslan == "ящерица")):
    print("Тимур")

elif (timur == "бумага" and (ruslan == "камень" or ruslan == "Спок")):
    print("Тимур")

elif (timur == "ящерица" and (ruslan == "бумага" or ruslan == "Спок")):
    print("Тимур")

elif (timur == "Спок" and (ruslan == "камень" or ruslan == "ножницы")):
    print("Тимур")

else:
    print("Руслан")