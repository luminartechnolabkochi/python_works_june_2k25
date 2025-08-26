
text="this is a python program to find most recursive word this python program is simple "

word_count = {}#{"this":2,}

words = text.split() 

for w in words:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)#{'this': 2, 'is': 2, 'a': 1, 'python': 2, 'program': 2, 'to': 1, 'find': 1, 'most': 1, 'recursive': 1, 'word': 1, 'simple': 1}



# method1 

# srt_wc=sorted(word_count,reverse=True,key=word_count.get)

max_val = max(word_count.values())

for k,v in word_count.items():

    if v == max_val:

        print(k,v)


# lambda functions
