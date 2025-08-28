

file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\employees.csv"

fr = open(file_path,"r")

all_employees = []

for line in fr:

    # removing \n from right side of line
    line = line.rstrip("\n")

    # split line in to data split by ,

    data = line.split(",")

    # create dictionary from data

    dictionary = {
        
                "id":data[0],"name":data[1],
                "department":data[2],"salary":data[3],
                "email":data[4],"location":data[5]                  
                  
                  }
    
    # append dictionary to employees list

    all_employees.append(dictionary)



print(all_employees)
    



