#Kypton Lantz
#February 17, 2025
#Module 8.2 Assignment: JSON Practice
#
#This program reads the student.json file, prints its original contents, and then updates the file with new data.

import json
import os

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Print the current working directory
print("Current working directory: ", os.getcwd())

#Function to print the student list
def print_student_list(student_list):
    for student in student_list:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

#Load the student.json file
with open('student.json') as f:
    data = json.load(f)

#Output notification to the user that this is the original student list
print('Original Student List:')
print_student_list(data)

#Add new student to the class list
new_student = {
    "F_Name": "Kypton",
    "L_Name": "Lantz",
    "Student_ID": 8675309,
    "Email": "k.lantz@email.com"
}
data.append(new_student)

#Output notification to the user that this is the updated student list
print('\nUpdated Student List:')
print_student_list(data)

#Write the updated data back to the student.json file
with open('student.json', 'w') as f:
    json.dump(data, f, indent=4)

#Output notification to the user that the student list has been updated
print('\nThe student.json file has been updated.')