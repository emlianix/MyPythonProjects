list1 = [int(input()) for i in input().split()]
mx_list = []

for el in list1:
	mx = max(el)
	mx_list.append(mx)

print(max(mx_list))