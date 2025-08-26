arr =[2,3,4,8,9,10]

# [expression iteration condition]

# map
# filter
# reduce min,max,sum,,,,
# generate new list map num as num+1 if num>5 else num-1

new_arr = [num+1 if num>5 else num-1 for num in arr ]

print(new_arr)


words=["apple","banana","carrot","drumstick","egg","fish"]


word_dictionary = {w:len(w) for w in words}

print(word_dictionary)

# create a new list of words starting with vowels

vowel_words = [w for w in words if w[0].lower() in "aeiou" ]

print(vowel_words)

# print longest word from words

longest_wotd=max(words,key=len)

print(longest_wotd)

shortest_word = min(words,key=len)

print(shortest_word)
