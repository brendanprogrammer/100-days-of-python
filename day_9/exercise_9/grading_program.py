'''
You have access to a database of student_scores in the format of a dictionary. 
The keys in student_scores are the names of the students and the values are their exam scores. 

Write a program that converts their scores to grades.

By the end of your program, you should have a new dictionary called student_grades that should 
contain student names as keys and their assessed grades for values. 

The final version of the student_grades dictionary will be checked. 

This is the scoring criteria: 

- Scores 91 - 100: Grade = "Outstanding" 
- Scores 81 - 90: Grade = "Exceeds Expectations" 
- Scores 71 - 80: Grade = "Acceptable" 
- Scores 70 or lower: Grade = "Fail" 
'''

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 91:
        grade = "Outstanding"
    elif score >= 81:
        grade = "Exceeds Expectations"
    elif score >= 71:
        grade = "Acceptable"
    else:
        grade = "Fail"
        
    #Add the student and their grade to student-grades
    student_grades[student] = grade
    
#4. Print the student_grades dictionary
print(student_grades)