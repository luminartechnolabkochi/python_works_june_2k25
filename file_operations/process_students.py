

all_students_path="C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\all_students.txt"

failed_students_path="C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\failed_studets.txt"

passed_students_path="C:\\Users\\Luminar\\Desktop\\development_journey_june\\python_works\\file_operations\\passeded_students.txt"


f_all_stud_ref = open(all_students_path,"r")

f_failed_ref = open(failed_students_path,"r")

f_passed_ref = open(passed_students_path,"w")

all_students_set=set()

failed_students_set=set()

for name in f_all_stud_ref:#hari/n

    all_students_set.add(name.rstrip("\n"))

print(all_students_set)


for name in f_failed_ref:

    failed_students_set.add(name.rstrip("\n"))

print(failed_students_set)

passed_students_set = all_students_set.difference(failed_students_set)

print(passed_students_set)


for name in passed_students_set:

    f_passed_ref.write(name+"\n")