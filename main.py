class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = [
            Contact("Alice", "1234567890", "alice@email.com"),
            Contact("Bob", "9876543210", "bob@email.com")
        ]

    def add_contact(self, name, phone_number, email):

        #This ADD contact isn't working...
        self.contacts.add(name, phone_number, email)
        print(f"Contact '{name}' added successfully.")

    def display_all_contacts(self):
        if self.contacts:
            print("All Contacts:")

            #Errors in code here
            for contact in contacts:
                print(f"Name: {name}\nPhone: {phone_number}\nEmail: {contact.email}\n")
        else:
            print("No contacts found.")

    #Missing SEARCH contact function

    #Missing UPDATE contact function

    #Missing DELETE cointact functions

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        #Missing options
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "0":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            #Needs code here to check incorrect user choice 
            print("")

if __name__ == "__main__":
    main()