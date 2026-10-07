import datetimefrom staff import staff
from ac import subjects

timetable=[]

def create_timetable():
    if len(staff)==0:
        print("no value")
        return
    print("Staff List")
    for i in staff:
        print(i["id"],i["name"],i["dep"])
    staff_id=int(input("Enter Staff ID:"))
    selected_staff=None
    for i in staff:
        if i["id"]==staff_id:
            selected_staff=i
            break
    if selected_staff is None:
        print("not found")
        return
    print("----Subjects List---")
    for i in subjects:
        print(i["code"],i["subject"])
    code=input("enter subject code")
    selected_subject=None
    for i in subjects:
        if i["code"]==code:
            selected_subject=i
            break
    if selected_subject is None:
        print("No subject")
        return
    day=input("Enter Day: ")
    period=input("Enter Period: ")
    current_datetime=datetime.datetime.now()
    created_date=current_datetime.strftime("%d-%m-%Y")
    created_time=current_datetime.strftime("%I:%M:%S %p")
    for j in timetable:
        if j["staff_id"]==staff_id and j["day"]==day and j["period"]==period:
            print("Conflict Detected")
            print("staff:",selected_staff["name"])
            print("day:",day)
            print("period:",period)
            return
    new_timetable={
        "staff_id":selected_staff["id"],
        "staff_name":selected_staff["name"],
        "subject_code":selected_subject["code"],
        "subject_name":selected_subject["subject"],
        "day":day,
        "period":period,
        "created_date":created_date,
        "created_time":created_time
    }
    timetable.append(new_timetable)
    print("Timetable created")
    print("Created Date:",created_date)
    print("Created Time:",created_time)

def view_staff_tt():
    if len(timetable)==0:
        print("No timetable available.")
        return
    staff_id=int(input("Enter Staff ID:"))
    found=False
    for k in timetable:
        if k["staff_id"]==staff_id:
            print("\nStaff:",k["staff_name"])
            print("Subject:",k["subject_name"])
            print("Day:",k["day"])
            print("Period:",k["period"])
            print("Created Date:",k["created_date"])
            print("Created Time:",k["created_time"])
            found=True
    if found==False:
        print("No timetable found.")

def view_complete_tt():
    if len(timetable)==0:
        print("No timetable available.")
        return
    for k in timetable:
        print("\nStaff:",k["staff_name"])
        print("Subject:",k["subject_name"])
        print("Day:",k["day"])
        print("Period:",k["period"])
        print("Created Date:",k["created_date"])
        print("Created Time:",k["created_time"])

def conflict():
    if len(timetable)==0:
        print("no value")
        return
    conflict_found=False
    for i in range(len(timetable)):
        for j in range(i+1,len(timetable)):
            one=timetable[i]
            two=timetable[j]
            if one["staff_id"]==two["staff_id"] and one["day"]==two["day"] and one["period"]==two["period"]:
                print("Conflict Found")
                print("Staff:",one["staff_name"])
                print("Subject1:",one["subject_name"])
                print("Subject2:",two["subject_name"])
                conflict_found=True
    if conflict_found==False:
        print("No conflicts found.")

def staff_workload():
    if len(staff)==0:
        print("no staff")
        return
    for i in staff:
        count=0
        for j in timetable:
            if j["staff_id"]==i["id"]:
                count=count+1
        print(i["id"],i["name"],":",count,"period")

def timetable_management():
    while True:
        print("1 Create Timetable")
        print("2 View Staff Timetable")
        print("3 View Complete Timetable")
        print("4 Conflict Detection")
        print("5 Staff Workload")
        print("6 Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            create_timetable()
        elif choice=="2":
            view_staff_tt()
        elif choice=="3":
            view_complete_tt()
        elif choice=="4":
            conflict()
        elif choice=="5":
            staff_workload()
        elif choice=="6":
            print("time table")
            break
        else:
            print("Invalid")

if __name__=="__main__":
    timetable_management()
