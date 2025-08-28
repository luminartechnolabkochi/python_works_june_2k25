

file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\employees.csv"

fr = open(file_path,"r")

all_employees = []

for line in fr:

    data = line.rstrip("\n").split(",")   

    # create dictionary from data

    dictionary = {
        
                "id":data[0],"name":data[1],
                "department":data[2],"salary":data[3],
                "email":data[4],"location":data[5]                  
                  
                  }
    
    # append dictionary to employees list

    all_employees.append(dictionary)



print(all_employees)
    

names = [e.get("name") for e in all_employees]

# print(names)


ekm_employees = [e.get("name") for e in all_employees if e.get("location") == "ekm"]

print(ekm_employees)

max_sal=max(all_employees,key=lambda e:e.get("salary"))

print(max_sal)

min_sal = min(all_employees,key=lambda e:e.get("salary")).get("salary")

min_sal_employees = [e.get("name") for e in all_employees if e.get("salary")==min_sal]

print(min_sal_employees)