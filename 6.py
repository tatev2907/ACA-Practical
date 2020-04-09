
MAX_CHAR = 26
def sortB(s, pat): 
	a=len(s)
	b=len(pat)
	ch=max(a,b)+1
	count = [0] * ch 
	print(count)
	for i in range (0, len(s)): 
		count[ord(s[i]) - 97] += 1
		print(count)

	index = 0; 
	s = "" 
	for i in range (0, len(pat)): 
		j = 0
		while(j < count[ord(pat[i]) - ord('a')]): 
			s += pat[i] 
			j = j + 1
			index += 1
	
	return s

s1= input("Input first string")
s2 = input("Input second string")
print(sortB(s1, s2)) 

