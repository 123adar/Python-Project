class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts
                   if search_term.lower() in contact.name.lower() or
                   search_term in contact.phone]
        return results

    def update_contact(self, old_name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == old_name.lower():
                self.contacts[i] = new_contact

    def delete_contact(self, contact_name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != contact_name.lower()]

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            print("\nContact List:")
            contact_book.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(search_term)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(f"Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            updated_name = input("Enter updated name: ")
            updated_phone = input("Enter updated phone number: ")
            updated_email = input("Enter updated email: ")
            updated_address = input("Enter updated address: ")
            updated_contact = Contact(updated_name, updated_phone, updated_email, updated_address)
            contact_book.update_contact(old_name, updated_contact)
            print("Contact updated successfully.")

        elif choice == '5':
            contact_name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(contact_name)
            print("Contact deleted successfully.")

        elif choice == '6':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()