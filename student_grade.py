student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades ={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for name in student_scores:
    print(student_scores[name])
    if student_scores[name]<=100 and student_scores[name]>=91:
        mark = "outstanding"
    elif student_scores[name]<=90 and student_scores[name]>=81:
        mark = "Exceeds Expectation"
    elif student_scores[name]<=80 and student_scores[name]>=71:
        mark = "Acceptable"
    elif student_scores[name]<=70:
        mark = "fail"   
    student_grades[name] = mark
    

# 🚨 Don't change the code below 👇
print(student_grades)