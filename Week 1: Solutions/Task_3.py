contacts = [{
    "Name": "Sachin Prabhu Ram",
    "Phone_Number": "82960619",
    "Email": "sachinpr@kth.se"
}]

def add_contacts(name, phone_num, email):
    contacts.append({"Name": name, "Phone_Number": phone_num, "Email": email})
    contact_id = len(contacts) - 1
    return contact_id

def display_contacts():
    for contact in contacts:
        print(f"Contact Information: ID {contacts.index(contact)}")
        print(f"Name: {contact['Name']}")
        print(f"Phone Number: {contact['Phone_Number']}")
        print(f"Email: {contact['Email']}")

def update_contacts(id, name, phone_num, email):
    contacts[id] = {"Name": name, "Phone_Number": phone_num, "Email": email}


contact_id = add_contacts("John Doe", "123-456-7890", "john@example.com")
_ = add_contacts("Alice Smith", "123-456-7777", "alice@example.com")
update_contacts(
    id=contact_id,
    name="John Doe",
    phone_num="555-555-5555",
    email="john@example.com"
)
display_contacts()