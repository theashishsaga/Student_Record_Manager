# 🎯 Project: Student Records Manager (Text-based App)
# ✅ Features:
# Add new student records
def add_student():
    name=input("enter student name:")
    roll=input("enter  roll number:")
    branch=input("enter branch:")

    with open("file.txt", "a") as f:
        f.write(f"{name},{roll},{branch}\n")

    print("✅ Record added!\n")

# View all student records
def view_student():
    try:
        with open("file.txt","r") as f:
            records=f.readlines()
            if not records:
                print("No record found")
            else:
                for record in records:
                    name,roll,branch=record.strip().split(",")
                    print(f"name:{name},roll no:{roll}, branch:{branch}")
    except FileNotFoundError:
        print("❌ No records file found.\n")
# Search student by name or roll number
def search_student():
    keyword=input("enter name or roll number to search").lower()
    found=False

    try:
        with open("file.txt","r") as f:
            for record in f:
                if keyword in record.lower():
                    name,roll,branch=record.strip().split(",")
                    print(f"🔍 Found → Name: {name}, Roll No: {roll}, Branch: {branch}")
                    found=True
        if not found:
            print("no matching student found")
    except FileNotFoundError:
        print("no record found.|n")

# Delete all records
def delete_all():
    confirm=input("are you sure wanT to delete all records?(yes\no)")
    if confirm.lower()=="yes":
        open("file.txt",'w').close()
        print("🗑️ All records deleted!\n")
    else:
        print("deletion cancelled.\n")


# Exit
def menu():
     while True:
        print("\n📚 Student Record Manager")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete All Records")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_all()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

menu()