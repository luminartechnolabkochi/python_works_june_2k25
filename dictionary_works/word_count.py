# word_count 


text = "hello hai hello hai hai"
words = text.split(" ")#['hello', 'hai', 'hello', 'hai', 'hai']

wc = {}#{"hello":2,"hai":1}

for w in words:#w=hello

    if w in wc:#"hello" in wc

        wc[w]+=1

    else:

        wc[w]=1

print(wc)

#text="ABCABB"

# display first recursive character

# A

# dictionary methods

    

    