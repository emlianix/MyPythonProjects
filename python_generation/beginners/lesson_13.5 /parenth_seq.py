def is_correct_bracket(text):
    count = 0
    for char in text:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        if count < 0:  # если закрывающая скобка появилась раньше открывающей
            return False
            
    return count == 0  # последовательность верна, только если все скобки закрыты

txt = input()
print(is_correct_bracket(txt))