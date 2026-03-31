Python 3.14.3 (v3.14.3:323c59a5e34, Feb  3 2026, 11:41:37) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
#Author: Sarah Gallagher
#File Name: student_gpa_app.py
#Description: This app accepts student names and GPAs to determin if they qualify for the Dean's List or Honor Roll.
>>> def main():
...     while True:
...         last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
...         # Check if the last name is 'ZZZ' to quit
...         if last_name == 'ZZZ':
...             break
...         first_name = input("Enter the student's first name: ")
...         gpa = float(input("Enter the student's GPA:"))
...         # Check for Dean's List qualification
...         if gpa >= 3.5:
...             print(f"{first_name} {last_name} has made the Dean's List!")
...         # Check for Honor Roll qualification
...         if gpa >= 3.25:
...             print(f"{first_name} {last_name} has made the Honor Roll!")
... 
...             
>>> main()
Enter the student's last name (or 'ZZZ' to quit): Doe
Enter the student's first name: John
Enter the student's GPA:3.6
John Doe has made the Dean's List!
John Doe has made the Honor Roll!
Enter the student's last name (or 'ZZZ' to quit): Smith
Enter the student's first name: Jane
Enter the student's GPA:3.3
Jane Smith has made the Honor Roll!
Enter the student's last name (or 'ZZZ' to quit): Gallagher
Enter the student's first name: Emily
Enter the student's GPA:3.2
Enter the student's last name (or 'ZZZ' to quit): Smith
Enter the student's first name: Bob
Enter the student's GPA:3.8
Bob Smith has made the Dean's List!
Bob Smith has made the Honor Roll!
Enter the student's last name (or 'ZZZ' to quit): Naglowsky
Enter the student's first name: Susan
Enter the student's GPA:3.25
Susan Naglowsky has made the Honor Roll!
