"""DigitV3"""
def digit():
    """func digit"""
    lst_word = input().split()
    num_lst = []
    word_dict ={
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
	'eleven': 11,
	'twelve': 12,
	'thirteen': 13,
	'fourteen': 14,
	'fifteen': 15,
	'sixteen': 16,
	'seventeen': 17,
	'eighteen': 18,
	'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
	'ninety': 90,
    'hundred': 100,
    'thousand': 1000
    }
    for i in lst_word:
        num_lst.append(word_dict[i])
    if len(num_lst) == 1:
        print(*num_lst)
    elif num_lst[1] == 100 or num_lst[1] == 1000:
        ans = (num_lst[0]*num_lst[1])+(sum(num_lst[2:]))
        print(ans)
    elif len(num_lst) == 2:
        ans = sum(num_lst)
        print(ans)
    elif num_lst[2] == 100 or num_lst[2] == 1000:
        ans = ((sum(num_lst[0:1]))*num_lst[2])+(sum(num_lst[3:]))
        print(ans)
digit()
