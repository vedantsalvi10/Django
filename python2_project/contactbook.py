class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = None
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.head = None

    def add_contact(self,name,email,phone):
        contact = Contact(name,phone,email)
        if self.head is None:
            self.head = contact
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = contact
    def view_contact(self):
       if self.head is None:
            print("No contacts added")
       else:
            current = self.head
            while current is not None:
                print(current)
                current = current.next
    def search_contact(self,name):
        if self.head is None:
            print("No contacts added")
            return
        else:
            current = self.head
            while current is not None:
                if current.name == name:
                     print(current)
                     return
                current = current.next
            print("This contact is not present")
    
    def delete_contact(self,name):
        if self.head is None:
            print("No contacts added")
            return
        elif self.head.name is name:
            self.head = self.head.next
            return
        else:
            current = self.head
            while current.next is not None:
                if current.name == name:
                     current.next = current.next.next
                     return
                current = current.next
            print("This contact is not present")

ContactBook = ContactBook()
ContactBook.add_contact("vedant","vedantsalvi@",542786345,)
ContactBook.add_contact("ram","ram@",5422386345,)
ContactBook.view_contact()
ContactBook.search_contact("vedant")
ContactBook.delete_contact("vedant")
ContactBook.view_contact()