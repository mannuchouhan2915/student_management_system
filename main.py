# student management system 
# features 

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

still = 'yes'
choice=int(input("enter your choice : "))
def add_student():
    pass 
def view_all_student():
    pass
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
    
    print(" do you want to continue : 'yes / no'")
    ans = input()
    still = ans 
        
    
    