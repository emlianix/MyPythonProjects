def is_palindrome(text):
    if text == text[::-1]:
    	return True
    else:
    	return False
    
    
def is_prime(num):
	if num <= 1:
		return False
	for i in range(2, num):
		if num % i == 0:
			return False
	return True
    
    
def is_valid_password(password):
	pass_list = password.split(':')
	if (
		len(pass_list) == 3
		and is_palindrome(pass_list[0])
		and is_prime(int(pass_list[1]))
		and int(pass_list[2]) % 2 == 0
	):
		return True
	else:
		return False
	
	
psw = input()
print(is_valid_password(psw))