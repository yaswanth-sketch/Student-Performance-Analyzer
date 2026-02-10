# Student-Performance-Analyzer
checking the given marks of students
Student Performance Analyzer
Program Overview

This Python program analyzes student internal marks and classifies their performance.
The marks are taken as input, stored in a list, and processed one by one using a for loop.

The program also counts:

Total valid students

Total failed students

At the end, a final summary is displayed.

Concepts Used

List

for loop

Conditional statements (if, elif, else)

String

Input and Output

Restrictions followed:

No max(), min(), sum()

No dictionary or set

No try-except

Classification Rules
Marks Range	Category
90 – 100	Excellent
75 – 89	Very Good
60 – 74	Good
40 – 59	Average
0 – 39	Fail
< 0 or > 100	Invalid
Personalization Logic

Personalization is based on the length of the student name.

name = "yaswanth"
name_length = len(name)


If the name length is even, (Checked) is printed along with the result.

If the name length is odd, the result is printed normally.

This personalization changes the program output and makes the logic unique.

How the Program Works

The user enters the number of students.

Marks are entered and stored in a list.

Each mark is checked and classified.

Valid students and failed students are counted.

Individual results and final summary are displayed.

Sample Output
Result
70 -> Good
35 -> Fail
110 -> Invalid

Final Summary
Total Valid Students: 2
Total Failed Students: 1

Author Details

Name: Yaswanth

Program: Student Performance Analyzer

Language: Python
