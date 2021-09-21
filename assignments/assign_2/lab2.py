print('**** Welcome to the LAB grade calculator! ****')
def setboundary(section, grade):
	if grade > 100:
		print(f'The {section} value should have been 100 or less. It has been changed to 100.')
		grade = 100
	elif grade < 0:
		print(f'The {section} value should have been zero or greater. It has been changed to zero')
		grade = 0

name = input('Who are we calculating grades for?\n')

labs_grade = float(input('Enter the labs grade:\n'))
if labs_grade > 100:
	print('The lab value should have been 100 or less. It has been changed to 100.')
	labs_grade = 100
elif labs_grade < 0:
	print('The lab value should have been zero or greater. It has been changed to zero')
	labs_grade = 0

exam_grade = float(input('Enter the exams grade:\n'))
if exam_grade > 100:
	print('The exam value should have been 100 or less. It has been changed to 100.')
	exam_grade = 100
elif exam_grade < 0:
	print('The exam value should have been zero or greater. It has been changed to zero')
	exam_grade = 0
attendance_grade = float(input('Enter the Attendance grade:\n'))
if attendance_grade > 100:
	print('The attendance value should have been 100 or less. It has been changed to 100.')
	attendance_grade = 100
elif attendance_grade < 0:
	print('The attendance value should have been zero or greater. It has been changed to zero')
	attendance_grade = 0

weighted_grade = labs_grade * 0.7 + exam_grade * 0.2 + attendance_grade * 0.1

def letter_grade(score):
    score = round(score)
    grades = [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')]
    for i in range(len(grades)):
        if score >= grades[i][0]:
            return grades[i][1]
print()
print('The weighted grade for', name, 'is', weighted_grade)
print(name, 'has a letter grade of', letter_grade(weighted_grade))
print()
print('**** Thanks for using the lab grade calculator ****')
print()
input('hit enter to end the program')









