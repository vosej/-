from hangul_jamo import compose
def gather(jamo_str):
	hangul=''.join(compose(jamo_str))
	return hangul


inputText = 'sorkrmflsrmfladms vosejrmfladlrh slrkrmflsrmfladms ansdjrmfladlek'

# 자음 (E는 English)
constant = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
constant_E = ['r', 'R', 's', 'e', 'E', 'f', 'a', 'q', 'Q', 't', 'T', 'd', 'w', 'W', 'c', 'z', 'x', 'v', 'g']

# 모음
vowel = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', ' ㅖ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ']     
vowel_E = ['k', 'o', 'i', 'O', 'j', 'p', 'u', 'P', 'h', 'y', 'n', 'b', 'm', 'l']

# 모음 합용자
mixed = ['ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']   
mixed_E = ['hk', 'ho', 'hl', 'nj', 'np', 'nl', 'ml']

# 받침 합용병서자
final = ['ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
final_E = ['fr', 'fa', 'fq', 'ft', 'fx', 'fv', 'fg', 'qt']


letters = ''
p = 0
while p < len(inputText):
	if p + 1 < len(inputText) and inputText[p:p+2] in mixed_E:
		letters += mixed[mixed_E.index(inputText[p:p+2])]
		p += 1
	elif inputText[p] in constant_E:
		letters += constant[constant_E.index(inputText[p])]
	elif inputText[p] in vowel_E:
		letters += vowel[vowel_E.index(inputText[p])]
	else:
		letters += inputText[p]
	p += 1
    
  print(gather(letters))
