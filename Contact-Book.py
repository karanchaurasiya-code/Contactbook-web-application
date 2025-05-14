Contact = {}

def create_contact():
    name = input("Enter contact name: ")
    if name in Contact:
        print(f"Contact name '{name}' already exists!")
    else:
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age. Please enter a number.")
            return
        email = input("Enter email id: ")
        mobile = input("Enter mobile number: ")
        Contact[name] = {'age': age, 'email': email, 'mobile': mobile}
        print(f"Contact '{name}' has been created successfully!")

def view_contact():
    name = input("Enter contact name to view: ")
    if name in Contact:
        info = Contact[name]
        print(f"Name: {name}")
        print(f"Age: {info['age']}")
        print(f"Email: {info['email']}")
        print(f"Mobile: {info['mobile']}")
    else:
        print("Contact not found!")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in Contact:
        try:
            age = int(input("Enter updated age: "))
        except ValueError:
            print("Invalid age. Please enter a number.")
            return
        email = input("Enter updated email id: ")
        mobile = input("Enter updated mobile number: ")
        Contact[name] = {'age': age, 'email': email, 'mobile': mobile}
        print(f"Contact '{name}' has been updated.")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in Contact:
        del Contact[name]
        print(f"Contact '{name}' has been deleted.")
    else:
        print("Contact not found!")

def search_contact():
    search_name = input("Enter contact name to search: ")
    if search_name in Contact:
        info = Contact[search_name]
        print(f"Name: {search_name}")
        print(f"Age: {info['age']}")
        print(f"Email: {info['email']}")
        print(f"Mobile: {info['mobile']}")
    else:
        print("Contact not found!")

def count_contacts():
    print(f"Total number of contacts: {len(Contact)}")

def view_all_contacts():
    if Contact:
        for name, info in Contact.items():
            print(f"Name: {name}, Age: {info['age']}, Email: {info['email']}, Mobile: {info['mobile']}")
    else:
        print("No contacts available.")

def main():
    while True:
        print("\n! Contact Book App !")
        print("1. Create contact")
        print("2. View contact")
        print("3. Update contact")
        print("4. Delete contact")
        print("5. Search contact")
        print("6. Count contact")
        print("7. View all contacts")
        print("8. Exit contact")
        print("---------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            search_contact()
        elif choice == "6":
            count_contacts()
        elif choice == "7":
            view_all_contacts()
        elif choice == "8":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
