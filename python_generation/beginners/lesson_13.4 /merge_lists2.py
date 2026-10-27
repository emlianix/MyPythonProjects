def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):  # прицепление остатка
        result += list1[p1:]
    else:  # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result


n = int(input())
# Считываем первый список
merged_list = [int(i) for i in input().split()]

# В цикле считываем остальные n - 1 списков и объединяем их
for _ in range(n - 1):
    current_list = [int(i) for i in input().split()]
    merged_list = quick_merge(merged_list, current_list)

print(*merged_list)