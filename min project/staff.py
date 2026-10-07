staff=[]

def add_staff():
    staff_id=int(input("Enter the staff ID:"))
    name=input("Enter the name:")
    Dep=input("Enter the dep:")
    new_staff={
        "id":staff_id,"name":name,"dep":Dep
        }
    staff.append(new_staff)
    print("staff is added")

def view_staff():
    if len(staff)==0:
        print("empty")
        return
    print("---staff list----")
    for i in staff:
        print("ID",i["id"])
        print("NAME",i["name"])
        print("DEP",i["dep"])

def staff_menu():
    while True:
        print("----college staff list-----")
        print("1 add staff")
        print("2 view staff")
        print("3 close")
        c=input("enter choice")
        if c=="1":
            add_staff()
        elif c=="2":
            view_staff()
        elif c=="3":
            print("closed")
            break
        else:
            print("invalid input")

if __name__=="__main__":
    staff_menu()
