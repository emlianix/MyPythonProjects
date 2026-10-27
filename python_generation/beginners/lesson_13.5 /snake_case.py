def convert_to_python_case(text):
    text_snake = ''
    
    for i in range(len(text)):
    	if text[i].isupper() and i != 0:
    		text_snake += '_' + text[i].lower()
    	else:
    		text_snake += text[i].lower()
    		
    return text_snake


txt = input()

print(convert_to_python_case(txt))