
file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\words.txt"

fw = open(file_path,"w")

words = ["hello","hai","madam","racecar","pangram"]


for w in words:

    if w == w[::-1]:

        fw.write(w+"\n")
