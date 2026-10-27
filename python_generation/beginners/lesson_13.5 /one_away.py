def is_one_away(word1, word2):
	if len(word1) != len(word2):
		return False
    	
	diff_cnt = 0
	for i in range(len(word1)):
		if word1[i] != word2[i]:
			diff_cnt += 1
	
	return diff_cnt == 1


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))