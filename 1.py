def isVowel(c):
    vowels = [ 'a', 'e', 'o', 'i', 'u','A', 'E', 'O', 'I', 'U' ]
    if c in vowels: 
        return True
    return False
def revVowel(s): 
    j = 0
    vowel = [0] * len(s) 
    s = list(s) 
    for i in range(len(s)): 
        if isVowel(s[i]): 
            vowel[j] = s[i] 
            j += 1
    for i in range(len(s)): 
        if isVowel(s[i]): 
            j -= 1
            s[i] = vowel[j] 
  
    return ''.join(s) 
  
if __name__ == "__main__": 
    s1=input()
    print(revVowel(s1)) 