from colorama import Fore, Style, init
# This command imported Fore (defining the text colour) and Style (defining the strength of the text) from Colorama.
# Additionally, Init (defining additional commands onto stylised text) got brought in to automatically reset the text once used.
init(autoreset=True)

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

        # This ADD contact arrived here not working.  The original message had .add at the end, which is an invalid method.
        # ".append" worked instead as a valid way to add something to the end of a list.
        # The next error was that list.append wanted one argument, of which I gave three, thanks to the class structure.
        # "Contact" and the three values in brackets got used for append, essentialy zipping the three inputs.
        # And as shown with the use of Style and Fore throughout, Colorama and various colors also got used.
            self.contacts.append(Contact(name,phone_number,email))
            print(Style.BRIGHT + Fore.GREEN + f"Contact '{name}' added successfully.")

    def display_all_contacts(self):
        if self.contacts:
            print(Style.BRIGHT + "All Contacts:")
            # The For loop below was originally "contact in contacts", but it wouldn't work without pulling from the class.
            # This is why "self." was needed to direct towards the class in particular.
            for contact in self.contacts:
            # All printed variables needed "contact." beforehand, not just the standard variable.
            # Only the email variable was printed correctly this way, hence "name" and "phone_number needed changing."
                print(Style.BRIGHT + Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
        else:
            print(Style.BRIGHT + Fore.RED + "No contacts found.")

    def duplicate_check(self):
        # This is a stretch goal that checked for duplicate by name entry and works in tandem with adding new contact.
        # There are also two Global values that would need to work with the Add code in the main code below.
        global duplicate
        global newname
        duplicate = False
        # A boolean value was needed to work with the If statement below.
        newname = input ("Enter name: ")
        for contact in self.contacts:
            # The below If statement would flip the duplicate trigger should any of the contact names match the input.
            if newname.capitalize() == contact.name:
                duplicate = True
                break
                
# Added Search function

    def search_contacts(self):
        # Many of these non-add functions check if self.contacts is true, which is needed to run in the first place.
        if self.contacts:
            searchname = input("Enter name: ")
            # Namecheck is another global and boolean checker, which would work in conjunction with the main code.
            global namecheck
            namecheck = True
            for contact in self.contacts:
            # Capitalize was used to check the name against the capitalized versions in the list in case the user is lazy.
                if searchname.capitalize() == contact.name:
            # The If statement above is needed to determine the value of Namecheck later on in the code.
            # The structure of this code is also used to trigger other boolean values when and if needed.
                    print(Style.BRIGHT + Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                    namecheck = True
                    break
                elif searchname not in contact.name:
                    namecheck = False
        # The Else statement below has a prompt for when there's nothing in the list to search for.
        else:
            print(Style.BRIGHT + Fore.RED + "The contact list is empty.")

    #Added Update contact function

    def update_contact(self):
        # Same as before, "if self.contacts" checks for contents in the address book.
        if self.contacts:
            updatename = input("Enter name: ")
            # The boolean variable "updatecheck" is needed to work in conjunction with the rest of the code.
            updatecheck = False
            # The boolean variable "promptgiven" is needed to confirm the user's choice in updating the contact.
            # Data can be very sensitive, so the more power to the user, the better.
            promptgiven = False
            for contact in self.contacts:
                if updatename.capitalize() == contact.name:
                    print(Style.BRIGHT + Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                    prompt = input("Change details? y/n")
                    # This y/n prompt works with the While loop below, which only breaks if a valid input is in place.
                    while promptgiven == False:
                        if prompt.lower() == "y":
                        # This is the event that the user press y (changed to lower in case the user has caps on).
                        # Here, new info gets inputted with different temporary variables.
                            new_phone = input("Enter phone number: ")
                            # There's a While loop here to check if the new phone number is entirely numbers.
                            while new_phone.isnumeric() is False:
                                new_phone = input("Invalid.  Enter phone number: ")
                            contact.phone_number = new_phone
                            new_email = input("Enter email: ")
                            contact.email = new_email
                            print(Style.BRIGHT + Fore.GREEN + f"Contact '{updatename}' has been changed.")
                            print(Style.BRIGHT + Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                            updatecheck = True
                            # The variable "updatecheck" is set to true after the user updated data.
                            break
                        elif prompt.lower() == "n":                            
                            updatecheck = True
                            # The variable "updatecheck" is also set to true if prompted to update, but said no.
                            break
                        else:
                            # There is code here for an invalid input, as long as a re-add for the prompt.
                            prompt = input(Style.BRIGHT + Fore.RED + "Invalid input.  Change details? y/n")
                elif updatename not in contact.name and updatecheck == False:
                # This Elif statement needed two checks.
                # If there's no matches during the For loop, the boolean "updatecheck" won't trigger.
                # This works along with the rest of the For loop.
                # Why?  It would otherwise always print because there's always one data that doesn't match.
                    print("User not found")
        else:
            # Error message in the event of empty list.
            print(Style.BRIGHT + Fore.RED + "The contact list is empty.")

    #Missing DELETE contact functions

    def delete_contact(self):
        # Same as before, self.contacts checks for content.
        if self.contacts:
            deletename = input("Enter name: ")
            # There is another global / boolean operator below to work with the Delete code.
            global delcheck
            delcheck = True
            # The variable "promptgiven" is back again to verify the user's choice.
            # Again, data is sensitive, and the power to delete things is a huge responsibility.
            promptgiven = False
            for contact in self.contacts:
                if deletename.capitalize() == contact.name:
                    print(Style.BRIGHT + Fore.YELLOW + f"Name: {contact.name}\nPhone: {contact.phone_number}\nEmail: {contact.email}\n")
                    prompt = input("Delete? y/n")
                    # There's another y/n prompt, along with a While loop that only breaks if a valid answer is put in.
                    while promptgiven == False:
                        if prompt.lower() == "y":
                            self.contacts.remove(contact)
                # The .remove method removes the highlighted contact in the For loop.
                # I also used a different color in Colorama, because Green is too positive for something like deletion.
                            print(Style.BRIGHT + Fore.BLUE + f"Contact '{deletename}' has been deleted")
                            delcheck = True
                            break
                        elif prompt.lower() == "n":                            
                            delcheck = True
                            break
                            # Just like in Update, delcheck turns to True if the y/n conditions are met.
                        else:
                            # This is the same invalid input message in the Update file.
                            prompt = input(Style.BRIGHT + Fore.RED + "Invalid input.  Change details? y/n")
                elif deletename not in contact.name:
                    namecheck = False
        else:
            print(Style.BRIGHT + Fore.RED + "The contact list is empty.")

    def sort_contact(self):
        # Sorting contacts is another stretch goal, and I wanted it to sort all contacts alphabetically.
        if self.contacts:
            # Of course, contacts needed to be in the address book to work.
            # The .sort function was needed to organize everything by the Name field.
            # How this works is that the Lambda function tells the .sort funciton to sort by a specific field.
            # In this case, "contact" got pulled, with contact.name being the field to sort the data.
            self.contacts.sort(key=lambda contact: contact.name)
            print(Style.BRIGHT + Fore.GREEN + "All contacts have been sorted alphabetically by name.")
        else:
            # If there's no data, there's no point to sort anything.
            print(Style.BRIGHT + Fore.RED + "No data to sort!")

def main():
    contact_book = ContactBook()

    while True:
        # All new options have been added in as they were placed in.
        print("\n--- Contact Book Menu ---")
        print("1. Add New Contact")
        print("2. Display Contacts")
        print("3. Search Contacts")
        print("4. Update Contacts")
        print("5. Delete Contacts")
        print("6. Sort Contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # The funciton "duplicate_check" was added in as a stretch goal.
            # So has the global boolean that worked with the rest of the code.
            contact_book.duplicate_check()
            if duplicate == False:
                name = newname.capitalize()
                phone_number = input("Enter phone number: ")
                # I added a While loop to check for pure numbers in the phone number.
                while phone_number.isnumeric() is False:
                    phone_number = input("Invalid.  Enter phone number: ")
                email = input("Enter email: ")
                contact_book.add_contact(name, phone_number, email)
            else:
    # If a duplicate already exists, the user doesn't put in the rest of the detail and goes back to the menu.
                print(Style.BRIGHT + Fore.RED + "This name entry already exists in our database.  Returning to menu.")
        elif choice == "2":
            contact_book.display_all_contacts()
        elif choice == "3":
            contact_book.search_contacts()
            # Because of the way of searching for contacts, namecheck was needed as a global variable.
            # This was in case there was nothing like what was typed in the database.
            if namecheck == False:
                print(Style.BRIGHT + Fore.RED + "User not found")
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
            # Similarly, delcheck was also needed as a global variable.
            # This was for the same reason for the content search - no data match.
            if delcheck == False:
                print(Style.BRIGHT + Fore.RED + "User not found")
        elif choice == "6":
            contact_book.sort_contact()
        elif choice == "0":
            print(Style.BRIGHT + Fore.CYAN + "Exiting Contact Book. Goodbye!")
            break
        else:
            # After the below print statement is printed, While is still true and we go back to the start.
            print(Style.BRIGHT + Fore.RED + "Invalid choice.  Please try again.")

# And this code down below ensures that everything is pulled from one file and not from others.
# The only exception is the Colorama library.
if __name__ == "__main__":
    main()