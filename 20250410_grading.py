student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

grades = {'Outstanding': [i for i in range(91, 101)],
          'Exceeds Expectations': [i for i in range(81, 91)],
          'Acceptable': [i for i in range(71, 81)],
          'Fail': [i for i in range(70)]
          }

student_grades = {}

for student in student_scores:
    student_score = student_scores[student]
    for grade in grades:
        student_grade_list = grades[grade]
        if student_score in student_grade_list:
            new_dict = {student: grade}
            student_grades.update(new_dict)
          
    
print(student_grades)