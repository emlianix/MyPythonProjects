num = int(input())
cnt = 0
total = 0

while True:
    total += 1
    if len(str(num)) > 7:
        cnt += 1

    if num % 100 == 11:
    	break
    	
    num = int(input())

print(cnt, '/', total, sep='')