# student management system 
# features 
import random
"""1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
"""
print("------ Welcome to student management system console ------")
print("what do you want to do ....? ")
print("""  1. Add Student 
           2. View All Students 
           3. Search Student 
           4. Update Student 
           5. Delete Student 
           6. Exit """)
student_dict={}
still = 'yes'
choice=int(input("enter your choice : "))

def add_student():
    student_id = int(input('enter student id : '))
    if student_id in student_dict:
        print('student of this id is already exists ....')
        print(student_dict[student_id])
    else:
        student_name=input('enter name : ')
        age=int(input('enter age : '))
        course = input('enter course : ')
        student_dict[student_id]={'Id ':student_id ,'Name':student_name ,'Age': age, 'Course':course}
        print("student added successfully...!")
def view_all_student():
    if len(student_dict) == 0:
        print("student list is empty")
    else:
        for k,v in student_dict.items():
            print(k," = " ,v)

        
def search_student():
    pass
def update_student():
    pass
def delete_student():
    pass
def exit():
    pass
while still !="no":
    if  choice == 1:
        add_student()
    elif choice == 2 :
        view_all_student()
    elif choice == 3:
        search_student()
    elif choice == 4 :
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        exit()
        break
    else :
        print(" your choice is worng ...")
    
   
    still = input(" do you want to continue : 'yes / no'\n")
    if still =='yes':
        choice = int(input('enter choice : '))
    
        
    
    