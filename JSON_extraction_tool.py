# Shrenik Bhatt

import json
import os

# This function imports a JSON file "student_courses", which is located in the same folder as this program.
# It then extracts course names and all the students taking that course and saves it in a text file named "output.txt"
# The new text file created is located in the same folder as this program.
# The program will also extract professor names as well as the students who have had the professor before.
# It will then save those in the same text file named "output.txt"


def main():
    student_courses = open('student_courses.json')
    file_data = json.load(student_courses)

    with open("output.txt", "a") as f:
        f.write("1) Sorting by students in each of the courses\n")
        f.close()

    for a in range(1, 10):
        name_list = []

        for q in file_data["courses"]:
            if (q["id"] == a):  # Print the professor names
                with open("output.txt", "a") as f:
                    f.write("\n"+str(q["name"])+": ")
                    f.close()

                for l in file_data["students"]:
                    # Checks to see if the student course list has course id of value a
                    if (a in l["courses"]):
                        # If it does, appends to list
                        name_list.append(str(l["name"]))

                with open("output.txt", "a") as f:
                    f.write(str(name_list)+"\n")
                    f.close()

    # Question 2, sorting names depending on professor name.
    prof_list = []
    values = []
    students = []

    # Make a list of the professors
    for q in file_data["courses"]:
        if (str(q["professor"]) not in prof_list):
            prof_list.append(str(q["professor"]))

    # Make a list of lists, where each inner list contains the course id values of courses taught by the same professor
    for a in range(0, len(prof_list)):
        value_list = []
        for q in file_data["courses"]:
            if(str(q["professor"]) == prof_list[a]):
                value_list.append(q["id"])
        values.append(value_list)

    # compare the values and make a list of lists, where each inner list has the students that a professor taught before
    for i in range(0, len(values)):
        student_list = []
        for l in file_data["students"]:
            check = any(k for k in values[i] if k in l["courses"])
            if (check and str(l["name"]) not in student_list):
                student_list.append(str(l["name"]))
        students.append(student_list)

    with open("output.txt", "a") as f:
        f.write(
            "\n\n 2) Sorting by students that had each of the professors previously\n")
        f.close()

    for i in range(0, len(prof_list)):
        with open("output.txt", "a") as f:
            f.write("\n" + str(prof_list[i])+": " + str(students[i])+"\n")
            f.close()

    print("Created file named 'output.txt' in same folder as this program file!")

    # This portion of the code should auto-open the file if it is run on a windows computer
    if os.name == 'nt':
        os.startfile("output.txt")


main()
