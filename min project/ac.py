subjects=[]

def add_subject():
    subject_code=input("enter the sub code:")
    sub_name=input("enter the name:")
    dep=input("enter department:")
    sem=input("enter semester:")
    hours=int(input("per week hours:"))
    subject={
        "code":subject_code,"subject":sub_name,
        "dep":dep,"sem":sem,"hours":hours
        }
    subjects.append(subject)
    print("subject is added")

def view_subject():
    print("-----subject List---")
    if len(subjects)==0:
        print("empty")
        return
    for i in subjects:
        print("\nSubject code :",i["code"])
        print("subject name:",i["subject"])
        print("dep:",i["dep"])
        print("Semester:",i["sem"])
        print("hours weeks:",i["hours"])

def search_subject():
    subject_name=input("Enter the subject name")
    for i in subjects:
        if i["subject"].lower()==subject_name.lower():
            print("subject")
            print("\nSubject code :",i["code"])
            print("subject name:",i["subject"])
            print("dep:",i["dep"])
            print("Semester:",i["sem"])
            print("hours weeks:",i["hours"])
            return
    print("not found")

def remove_subject():
    code=input("Enter subject code: ")
    for i in subjects:
        if i["code"]==code:
            subjects.remove(i)
            print("Subject Removed")
            return
    print("Subject not found.")

def academic():
    while True:
        print("1 add Subject")
        print("2 view Subject")
        print("3 search Subject")
        print("4 removeSubject")
        print("5 exit")
        c=input("Enter your choice: ")
        if c=="1":
            add_subject()
        elif c=="2":
            view_subject()
        elif c=="3":
            search_subject()
        elif c=="4":
            remove_subject()
        elif c=="5":
            print("Closed")
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    academic()
