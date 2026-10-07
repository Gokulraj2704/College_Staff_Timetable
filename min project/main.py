from staff import staff_menu
from ac import academic
from timetable import timetable_management
import pandas as pd
def main():
    while True:
        print("COLLEGE STAFF TIMETABLE SYSTEM")
        print("1. Staff")
        print("2. Academic")
        print("3. Timetable")
        print("4. Exit")
        choice=input("Enter your choice:")
        if choice=="1":
            staff_menu()
        elif choice=="2":
            academic()
        elif choice=="3":
            timetable_management()
        elif choice=="4":
            print("Closed")
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    main()
