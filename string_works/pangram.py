

# write a program to chk given string is pangram
text ="The quick brown fox jumps over the lazy dog".casefold()


alphabets="abcdefghijklmnopqrstuvwxyz"

is_pangram = True


for ch in alphabets:

    if ch not in text:

        is_pangram = False

        break

print(is_pangram)


word1="ABC"

word2="PQR"

# merge string
#APBQCR