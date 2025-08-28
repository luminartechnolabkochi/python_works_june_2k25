
file_path="C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\greetings.txt"

fa = open(file_path,"a")

food_items=["idly","tea","dosa"]


for item in food_items:

    fa.write(item+"\n")

