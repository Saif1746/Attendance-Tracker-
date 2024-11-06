# Attendance-Tracker-

Basic Attendance Tracker in python

A simple Python-based attendance tracking program that allows you to add and view attendance records for students across different subjects. This project is helpful for basic record-keeping and can be easily extended for more functionalities.

## Features

 ### 1. Add Attendance: 
Add attendance records for students, including their names, subjects, and dates.

 ### 2. View Attendance:

   Summary: See a count of attendance records per student and subject.

   Detail: View the entire list of attendance entries.

### How to Use

1. Run the Program: Start the script to access the main menu.

2. Choose an Action:

Type 1 to add a new attendance record.

Type 2 to view attendance (summary or detailed).

### Add Attendance:

Enter the student's name, subject (Eng, Math, Chem), and date (dd/mm/yy format).

### View Attendance:

Choose "summary" to view a summarized count of attendance by student and subject.

Choose "detail" to view each attendance entry in full.

### Program Walkthrough

The get_input() function is the main menu where users choose to either add or view attendance.

The add() function prompts for the student’s name, subject, and date, then writes this data to attendance.txt.

The view() function allows users to view either a summary or a detailed record:

summary: Displays the number of attendance entries per student for each subject.

detail: Lists each attendance entry line-by-line.

### Code Details

File Management: Attendance records are stored in attendance.txt, allowing easy file reading and appending.

Dictionary Usage: For the summary view, a dictionary (dic) is used to count attendance entries for each student-subject pair.

Example:

Adding Attendance:

Enter the name of the student: Alice
Enter the subject for which the attendance is to be added [Eng, Math, Chem]: eng
Enter the date in dd/mm/yy format: 01/11/24

Viewing Attendance Summary:

Alice appears 3 time(s) for the subject Eng
Bob appears 2 time(s) for the subject Math

