
file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\jobs.csv"


fr = open(file_path,"r")

for line in fr:

    data = line.rstrip("\n").split(",")

    print(data)


