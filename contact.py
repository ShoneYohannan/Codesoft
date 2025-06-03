# 🗂️ Unique CLI Contact Manager

contact_list = []

def add_contact():
    print("\n📌 Add New Contact")
    name = input("👤 Name        : ")
    phone = input("📞 Phone       : ")
    email = input("📧 Email       : ")
    address = input("🏠 Address     : ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }

    contact_list.append(contact)
    print(f"\n✅ Contact '{name}' added successfully!")

def display_contacts():
    print("\n📇 Contact List")
    if not contact_list:
        print("🚫 No contacts saved.")
    else:
        for i, contact in enumerate(contact_list):
            print(f"{i}. {contact['name']} | {contact['phone']}")

def search_contact():
    print("\n🔍 Search Contact")
    query = input("Enter name or phone: ").lower()
    found = False

    for contact in contact_list:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\n✅ Match Found:")
            print(f"👤 Name    : {contact['name']}")
            print(f"📞 Phone   : {contact['phone']}")
            print(f"📧 Email   : {contact['email']}")
            print(f"🏠 Address : {contact['address']}")
            found = True
            break

    if not found:
        print("⚠️ No matching contact found.")

def update_contact():
    print("\n✏️ Update Contact")
    display_contacts()

    try:
        index = int(input("Enter contact number to update: "))
        if 0 <= index < len(contact_list):
            current = contact_list[index]
            print("\nLeave blank to keep existing values:")

            name = input(f"👤 Name [{current['name']}]: ") or current['name']
            phone = input(f"📞 Phone [{current['phone']}]: ") or current['phone']
            email = input(f"📧 Email [{current['email']}]: ") or current['email']
            address = input(f"🏠 Address [{current['address']}]: ") or current['address']

            contact_list[index] = {
                'name': name,
                'phone': phone,
                'email': email,
                'address': address
            }

            print("✅ Contact updated successfully.")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_contact():
    print("\n🗑️ Delete Contact")
    display_contacts()

    try:
        index = int(input("Enter contact number to delete: "))
        if 0 <= index < len(contact_list):
            removed = contact_list.pop(index)
            print(f"🗑️ Contact '{removed['name']}' deleted.")
        else:
            print("❌ Invalid contact number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def show_menu():
    print("\n📘 Contact Manager")
    print("1️⃣  Add Contact")
    print("2️⃣  View Contact List")
    print("3️⃣  Search Contact")
    print("4️⃣  Update Contact")
    print("5️⃣  Delete Contact")
    print("6️⃣  Exit")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("🔸 Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            display_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye! Have a nice day.")
            break
        else:
            print("⚠️ Invalid choice. Please enter a number from 1 to 6.")
