#Name:Yu-Wei Chang
#File name: M02CaseStudy
#Purpose: Apply the knowledge and skill in coding if...else and while statements in Python

while True:
    last_name = input("Enter student's last name (enter 'ZZZ' to quit): ")
    if last_name == 'ZZZ':
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else :
        print(f"{first_name} {last_name} did not make into Dean's List or Honor Roll.")

