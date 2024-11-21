class ContactBook:
    def __init__(self):
        self.contacts = []  # List to store contacts

    def add_contact(self):
        """Add a new contact."""
        print("\n--- Add New Contact ---")
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        # Add to contacts list
        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """View all saved contacts."""
        print("\n--- Contact List ---")
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")

    def search_contact(self):
        """Search for a contact by name or phone number."""
        print("\n--- Search Contact ---")
        search_term = input("Enter name or phone number to search: ").strip().lower()
        found_contacts = [c for c in self.contacts if search_term in c["name"].lower() or search_term in c["phone"]]

        if not found_contacts:
            print("No matching contacts found.")
        else:
            print("\n--- Search Results ---")
            for contact in found_contacts:
                self.display_contact(contact)

    def update_contact(self):
        """Update an existing contact."""
        print("\n--- Update Contact ---")
        search_term = input("Enter name or phone number of the contact to update: ").strip().lower()
        for contact in self.contacts:
            if search_term in contact["name"].lower() or search_term in contact["phone"]:
                print("Contact found:")
                self.display_contact(contact)
                print("\nEnter new details (leave blank to keep unchanged):")
                contact["name"] = input(f"Name [{contact['name']}]: ").strip() or contact["name"]
                contact["phone"] = input(f"Phone [{contact['phone']}]: ").strip() or contact["phone"]
                contact["email"] = input(f"Email [{contact['email']}]: ").strip() or contact["email"]
                contact["address"] = input(f"Address [{contact['address']}]: ").strip() or contact["address"]
                print("Contact updated successfully.")
                return
        print("No matching contact found.")

    def delete_contact(self):
        """Delete a contact."""
        print("\n--- Delete Contact ---")
        search_term = input("Enter name or phone number of the contact to delete: ").strip().lower()
        for contact in self.contacts:
            if search_term in contact["name"].lower() or search_term in contact["phone"]:
                self.contacts.remove(contact)
                print(f"Contact '{contact['name']}' deleted successfully.")
                return
        print("No matching contact found.")

    def display_contact(self, contact):
        """Display a contact's details."""
        print(f"\nName: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

    def run(self):
        """Main menu loop."""
        while True:
            print("\n--- Contact Book Menu ---")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.update_contact()
            elif choice == "5":
                self.delete_contact()
            elif choice == "6":
                print("Exiting Contact Book. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    app = ContactBook()
    app.run()
