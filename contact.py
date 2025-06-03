contacts=[]

def add_contact():
    name=input("enter the contact name:")
    phone=input("enter the phone number:")
    email=input("enter the email address")
    address = input("enter the address:")

    contact={
        'name':name,
        'phone':phone,
        'email':email,
        'address':address
    }

    contacts.append(contact)
    print(f"\nContact {name} added ")



def view_contacts():
    if not contacts:
        print("\nNo contact found,")

    else:
        print("\n--- Contacts List ---")
        for index,contact in enumerate(contacts):
            print(f"{index}.{contact['name']} | {contact['phone']}")



def search_contact():
    keyword=input("enter name or phone number to search :").lower()
    found=False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["Phone"]:
            print("\n-- Contact Found ---")
            print(f" Name :{contact['name']}")    
            print(f"phone: {contact['phone']}")
            print(f" Email: {contact['email']}")
            print(f" Address :{contact['address']}")
            found=True
    if not found:
        print("no matching contact ")



def update_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to update: "))
        if 0 <= index < len(contacts):
            print("\nEnter new details (leave blank to keep current):")
            name = input(f"Name [{contacts[index]['name']}]: ") or contacts[index]['name']
            phone = input(f"Phone [{contacts[index]['phone']}]: ") or contacts[index]['phone']
            email = input(f"Email [{contacts[index]['email']}]: ") or contacts[index]['email']
            address = input(f"Address [{contacts[index]['address']}]: ") or contacts[index]['address']
            
            contacts[index] = {
                "name": name,
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: "))
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Contact '{removed['name']}' deleted.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")



def menu():
    print("\n -- Contact book ---")
    print("1. Add contact")
    print("2. View contact list")
    print("3.Search contact ")
    print("4 .Update contact ")
    print("5.Delete contact")
    print("6.Exit")



if __name__ =="__main__":
    while True:
        menu()
        choice =input("enter your choice ")

        if choice == "1":
            add_contact()
        elif choice =="2":
            view_contacts()
        elif choice =="3":
            search_contact()
        elif choice=="4":
            update_contact()
        elif choice =="5":
            delete_contact()
        elif choice=="6":
            print("Goodbye!")
            break
        else:
            print("invalid input")



