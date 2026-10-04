# Week 3 - Contact Management System
# Python Internship Project - The Developers Arena

import json
import csv
import re
from pathlib import Path

DATA_FILE = "contacts.json"


def load_contacts():
    """Load contacts from JSON file."""
    if not Path(DATA_FILE).exists():
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not load contacts. Starting with an empty list.")
        return {}


def save_contacts(contacts):
    """Save contacts to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(contacts, file, indent=4)
        return True
    except OSError:
        print("Error: Could not save contacts.")
        return False


def valid_phone(phone):
    """Validate a phone number with 10-15 digits."""
    digits = re.sub(r"\D", "", phone)
    return 10 <= len(digits) <= 15


def valid_email(email):
    """Basic email validation."""
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


def get_non_empty(prompt):
    """Get non-empty text from the user."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_phone():
    """Get a valid phone number."""
    while True:
        phone = input("Phone: ").strip()
        if valid_phone(phone):
            return phone
        print("Please enter a valid phone number (10-15 digits).")


def get_email():
    """Get a valid email address."""
    while True:
        email = input("Email: ").strip()
        if valid_email(email):
            return email
        print("Please enter a valid email address.")


def add_contact(contacts):
    """Add a new contact."""
    name = get_non_empty("Name: ")

    if name in contacts:
        print("A contact with this name already exists.")
        return

    phone = get_phone()
    email = get_email()
    address = get_non_empty("Address: ")
    group = get_non_empty("Group (Friends/Family/Work): ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
        "group": group
    }

    save_contacts(contacts)
    print("Contact added successfully.")


def search_contacts(contacts):
    """Search contacts by partial name."""
    query = input("Search name: ").strip().lower()

    if not query:
        print("Search cannot be empty.")
        return

    matches = {
        name: info for name, info in contacts.items()
        if query in name.lower()
    }

    if not matches:
        print("No matching contacts found.")
        return

    print("\nSearch Results")
    print("-" * 45)

    for number, (name, info) in enumerate(matches.items(), 1):
        print(f"{number}. {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email']}")
        print(f"   Address: {info['address']}")
        print(f"   Group: {info['group']}")
        print()


def update_contact(contacts):
    """Update an existing contact."""
    search_name = input("Enter the contact name to update: ").strip().lower()

    matches = [name for name in contacts if search_name in name.lower()]

    if not matches:
        print("No matching contact found.")
        return

    if len(matches) > 1:
        print("Multiple matches found:")
        for i, name in enumerate(matches, 1):
            print(f"{i}. {name}")

        try:
            choice = int(input("Select contact number: "))
            if choice < 1 or choice > len(matches):
                print("Invalid selection.")
                return
            name = matches[choice - 1]
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        name = matches[0]

    contact = contacts[name]

    print("Press Enter to keep the current value.")
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    address = input(f"Address [{contact['address']}]: ").strip()
    group = input(f"Group [{contact['group']}]: ").strip()

    if phone:
        if valid_phone(phone):
            contact["phone"] = phone
        else:
            print("Invalid phone. Old phone number kept.")

    if email:
        if valid_email(email):
            contact["email"] = email
        else:
            print("Invalid email. Old email kept.")

    if address:
        contact["address"] = address

    if group:
        contact["group"] = group

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    """Delete a contact after confirmation."""
    name = input("Enter contact name to delete: ").strip()

    matches = [contact_name for contact_name in contacts
               if name.lower() in contact_name.lower()]

    if not matches:
        print("No matching contact found.")
        return

    if len(matches) > 1:
        print("Multiple matches found:")
        for i, contact_name in enumerate(matches, 1):
            print(f"{i}. {contact_name}")
        try:
            choice = int(input("Select contact number: "))
            if 1 <= choice <= len(matches):
                name = matches[choice - 1]
            else:
                print("Invalid selection.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return
    else:
        name = matches[0]

    confirm = input(f"Delete '{name}'? (y/n): ").strip().lower()

    if confirm == "y":
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Deletion cancelled.")


def view_all_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("No contacts available.")
        return

    print("\nAll Contacts")
    print("=" * 60)

    for number, (name, info) in enumerate(contacts.items(), 1):
        print(f"{number}. {name}")
        print(f"   Phone: {info['phone']}")
        print(f"   Email: {info['email']}")
        print(f"   Address: {info['address']}")
        print(f"   Group: {info['group']}")
        print("-" * 60)


def export_csv(contacts):
    """Export contacts to a CSV file."""
    if not contacts:
        print("No contacts to export.")
        return

    try:
        with open("contacts_export.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Address", "Group"])

            for name, info in contacts.items():
                writer.writerow([
                    name,
                    info["phone"],
                    info["email"],
                    info["address"],
                    info["group"]
                ])

        print("Contacts exported to contacts_export.csv")
    except OSError:
        print("Error: Could not export contacts.")


def show_statistics(contacts):
    """Display contact statistics."""
    total = len(contacts)

    groups = {}
    for info in contacts.values():
        group = info.get("group", "Other")
        groups[group] = groups.get(group, 0) + 1

    print("\nStatistics")
    print("-" * 30)
    print(f"Total Contacts: {total}")

    for group, count in groups.items():
        print(f"- {group}: {count} contacts")


def show_menu():
    """Display the main menu."""
    print("\n" + "=" * 45)
    print("        CONTACT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Export to CSV")
    print("7. View Statistics")
    print("8. Exit")


def main():
    contacts = load_contacts()

    print("=" * 45)
    print("        CONTACT MANAGEMENT SYSTEM")
    print("=" * 45)

    while True:
        show_menu()

        try:
            choice = input("Enter your choice (1-8): ").strip()

            if choice == "1":
                add_contact(contacts)
            elif choice == "2":
                search_contacts(contacts)
            elif choice == "3":
                update_contact(contacts)
            elif choice == "4":
                delete_contact(contacts)
            elif choice == "5":
                view_all_contacts(contacts)
            elif choice == "6":
                export_csv(contacts)
            elif choice == "7":
                show_statistics(contacts)
            elif choice == "8":
                save_contacts(contacts)
                print("Thank you for using the Contact Management System!")
                break
            else:
                print("Invalid choice. Please select 1-8.")

        except KeyboardInterrupt:
            print("\nProgram stopped safely.")
            save_contacts(contacts)
            break
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
