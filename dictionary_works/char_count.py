text="goodmorning"

char_count = {}

for ch in set(text):

    char_count[ch]=text.count(ch)

print(char_count)#{'d': 1, 'r': 1, 'o': 3, 'm': 1, 'g': 2, 'n': 2, 'i': 1}

max_frequency = 0

max_frequency_dictionary = {}

for k,v in char_count.items():

    if v > max_frequency:

        max_frequency = v

        max_frequency_dictionary.clear()

        max_frequency_dictionary[k]=v

print(max_frequency_dictionary)


