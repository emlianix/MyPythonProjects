is_non_negative_num = lambda s: s.replace('.', '', 1).isdigit()

is_num = lambda s: is_non_negative_num(s) or (s.startswith('-') and is_non_negative_num(s[1:]))