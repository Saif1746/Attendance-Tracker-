print("****Attendance Tracker****")

def get_input():
    while True:
        print("What do you want to do?:")
        user = input("1. Add attendance \n2. View attendance: ")
        if user == "1":
            add()
            break
        elif user == "2":
            view()
            break
        else:
            print("Invalid Ketyword. Please type 1 or 2 for the respective options.")

def subject():
    while True:
        s = input("Enter the subject for which the attendance is to be added [Eng, Math, Chem]: ").lower()
        if s in ["eng", "math", "chem"]:
            return s
        else:
            print("Invalid Keyword")

def add():
    name = input("Enter the name of the student: ").title()
    sub = subject()
    date = input("Enter the date in dd/mm/yy format: ")

    with open("attendance.txt", "a") as f:
        f.write(name + ", " + sub + ", " + date + "\n")


dic = {}

def view():
    inp = view_func()
    
    while True:
        if inp == "summary":
            with open("attendance.txt", "r") as f:
                for i in f.readlines():
                    name, sub, date = i.split(",")
                    key = (name, sub)

                    if key in dic:
                        dic[key] += 1
                    else:
                        dic[key] = 1    
        
            for key,  j in dic:
                print(f"{key} appears {dic[key, j]} time(s) for the subject {j.strip().title()} ")
            break
        
        elif inp == "detail":
            with open("attendance.txt", "r") as f:
                for line in f:
                    print(line.rstrip())
            break
        else:
            print("Invalid Keyword")
                
    
def view_func():
    while True:
        inp = input(("Do you want to view all the detailed attendance or summary? (detail, summary): ")).lower()
        if inp in ["detail", "summary"]:
            return inp
        else:
            print("Invalid Keyword")



get_input()




    
