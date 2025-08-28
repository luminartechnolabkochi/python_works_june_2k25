

file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\greetings.txt"

fw = open(file_path,"w")

greetings_list = ["Good morning","good afternoon","good evening"]

for g in greetings_list:

    fw.write(g+"\n")
