def get_unique(numbers):
    new = []
    for n in numbers:
    	if n not in new:
    		new.append(n)
    return new

num = eval(input())
print(get_unique(num))