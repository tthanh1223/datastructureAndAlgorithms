import json
import os
class ContactsManager:
    def __init__(self,filename = 'contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as json_file:
                contacts = json.load(json_file)
                return contacts
        return []

    def save_contacts(self):
        """Save contacts to JSON file"""
        with open(self.filename, 'w') as json_file:
            json.dump(self.contacts, json_file, indent = 4)

    def create_contact(self,name, phone):
        """Create a new contact to add into the list"""
        new_contact = {'name':name,'phone': phone}
        self.contacts.append(new_contact)
        self.save_contacts()
        print(f'Contact {name} added')

    def read_contacts(self):
        """Print all the contacts"""
        if not self.contacts:
            print('There are no contacts')
        print("Contacts:".center(20,'-'))
        for idx, contact in enumerate(self.contacts,start = 1):
            print(f"{idx}. {contact['name']}: {contact['phone']}")

    def update_contact(self,index,name,phone):
        """Update an existing contact by index"""
        if 0 <= index < len(self.contacts):
            self.contacts[index]['name'] = name
            self.contacts[index]['phone'] = phone
            self.save_contacts()
            print(f'Contact at {index} updated')
        else:
            print(f'Invalid index')

    def delete_contact(self, args):
        """Delete an existing contact by index or name."""
        if isinstance(args, int):  # Check if args is an index
            index = args
            if 0 <= index < len(self.contacts):
                removed_contact = self.contacts.pop(index)
                self.save_contacts()
                print(f"Contact '{removed_contact['name']}' deleted.")
            else:
                print("Invalid index.")

        elif isinstance(args, str):  # Check if args is a name
            # Search for the contact by name
            for i, contact in enumerate(self.contacts):
                if contact['name'].lower() == args.lower():  # Case-insensitive comparison
                    removed_contact = self.contacts.pop(i)
                    self.save_contacts()
                    print(f"Contact '{removed_contact['name']}' deleted.")
                    return

            print(f"Contact '{args}' not found.")

def main():
    manager = ContactsManager()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n--- Contacts Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            manager.create_contact(name, phone)
        elif choice == '2':
            manager.read_contacts()
        elif choice == '3':
            index = int(input("Enter the index of the contact to update: ")) - 1
            name = input("Enter new name: ")
            phone = input("Enter new phone number: ")
            manager.update_contact(index, name, phone)
        elif choice == '4':
            index = input("Enter the index of the contact to delete: ")
            if isinstance(index,int):
                index = int(index) - 1
            manager.delete_contact(index)

        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





