

file_path = "C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\food_logs.csv"

fr = open(file_path,"r")

food_logs = []

for line in fr:#2025-08-22,Breakfast,Poha,1 plate,280\n


    data = line.rstrip("\n").split(",")  

    if len(data)>1:

        dictionary = {
            "date":data[0],
            "meal_type":data[1],
            "name":data[2],
            "serving_size":data[3],
            "calories":data[4]

        }

        food_logs.append(dictionary)

print(food_logs)

daily_summary ={}

for e in food_logs:

    date = e.get("date")

    calories = int(e.get("calories"))

    if date in daily_summary:

        daily_summary[date]+=calories

    else:

        daily_summary[date] = calories

print(daily_summary)


# Topic for tomorrow : Decision making (if..else,if elif,else)


# Task .csv
