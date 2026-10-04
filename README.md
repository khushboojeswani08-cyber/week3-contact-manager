# Contact Management System

## Project Description
This is a Python-based Contact Management System created for Week 3 of The Developers Arena internship.

The program allows users to add, search, update, delete and view contacts. It also saves contacts in a JSON file and can export them to CSV.

## What I Learned
1. Functions - creating reusable and organized code
2. Dictionaries - storing contact information as key-value pairs
3. String methods - formatting and searching text
4. File operations - reading and writing JSON/CSV files
5. Input validation - checking phone numbers, emails and empty input
6. Error handling - handling invalid input and file errors

## Features
- Add new contacts with validation
- Search contacts by partial name
- Update existing contact information
- Delete contacts with confirmation
- View all contacts
- Save contacts automatically to JSON
- Load contacts when the program starts
- Export contacts to CSV
- View contact statistics
- Phone and email validation
- User-friendly menu
- Error handling for operations

## How to Run

Make sure Python 3 is installed.

```bash
python contacts_manager.py
```

To run the tests:

```bash
python test_contacts.py
```

## Data Structure

Each contact is stored in a dictionary:

```python
contacts = {
    "John Doe": {
        "phone": "+1234567890",
        "email": "john@example.com",
        "address": "123 Main St",
        "group": "Friends"
    }
}
```

## Sample Menu

```text
=============================================
        CONTACT MANAGEMENT SYSTEM
=============================================
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit
```

## Sample Contact

```text
Name: John Doe
Phone: +1234567890
Email: john@example.com
Address: 123 Main St
Group: Friends
```

## Challenges & Solutions

### Challenge 1: Duplicate contact names
Solution: The program checks whether a name already exists before adding a new contact.

### Challenge 2: Phone number validation
Solution: A validation function checks for 10-15 digits and supports common formatting.

### Challenge 3: Partial search
Solution: The program uses lowercase comparison so users can search by part of a name.

### Challenge 4: Data persistence
Solution: Contacts are stored in a JSON file and loaded automatically when the program starts.

### Challenge 5: File errors
Solution: JSON and CSV operations use error handling so the program does not crash unexpectedly.

## Quality Standards Checklist

- Project Overview: Included
- Setup Instructions: Included
- Code Structure: Organized using functions
- Visual Documentation: Add screenshots after running the program
- Technical Details: Functions, dictionaries, JSON and CSV explained
- Testing Evidence: test_contacts.py included

## Project Files

```text
week3-contact-manager/
|-- contacts_manager.py
|-- test_contacts.py
|-- README.md
|-- .gitignore
```

## Author
Khushboo Jeswani

## Internship
The Developers Arena - Python Internship
