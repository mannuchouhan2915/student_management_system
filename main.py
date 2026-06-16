import random
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
        print('student of this id is already exists ....😊')
        print(student_dict[student_id])
        print()
    else:
        student_name=input('enter name : ')
        age=int(input('enter age : '))
        course = input('enter course : ')
        student_dict[student_id]={'Id ':student_id ,'Name':student_name ,'Age': age, 'Course':course}
        print("student added successfully...!😊")
        print()

def view_all_student():
    if len(student_dict) == 0:
        print("student list is empty 😒")
        print()
    else:
        for k,v in student_dict.items():
            print(k," = " ,v)
        print()
        
def search_student():
    id = int(input('enter student id :\t'))
    if id in student_dict :
        print('Student Found ..')
        print(student_dict[id])
        print()
    else:
        print('Student does not exists.. 👎')
        print()

def update_student():
    id = int(input('enter student id for update :\t'))
    if id in student_dict :
        curr_name = input('enter new name :\t')
        curr_age = int(input("enter new age :\t"))
        curr_course= input('enter new course name :\t ')
        student_dict[id]={'Name':curr_name ,'Age': curr_age, 'Course':curr_course}
        print('student details updated successfully ...!😊')
        print()
    

def delete_student():
    id =int(input('enter student id you want to delete :\t'))
    if id in student_dict :
        ans=input('Are you sure ? (y/n)\t')
        if ans == 'y':
            student_dict.pop(id)
            print('Student deleted successfully !👍')
            print()
        else:
            print('Deletion cancelled 😒')
    else:
        print('Student does not exists.. 👎')
        print()

def exit():
    print('THANK YOU FOR USING STUDENT MANAGEMENT SYSTEM ❤️')
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
        print("your choice is worng ...😒")
        print()
    
   
    still = input("do you want to continue : 'yes / no'\n")
    print()
    if still =='yes':
        choice = int(input('enter choice : '))
    else:
        print('THANK YOU FOR USING STUDENT MANAGEMENT SYSTEM ❤️')

        
    
    