class contact:
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
class ContactManager:
    def __init__(self):
        self.contacts=[]
    def add_contact(self,contact):
        self.contacts.append(contact)
    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name:{contact.name},phone:{contact.phone},email:{contact.email}")
    def search_contact(self,query):
        results=[]
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results
    def update_contact(self,old_contact,new_contact):
       index=self.contacts.index(old_contact)
       self.contacts[index]=new_contact

    def delete_contact(self,contact):
        self.contacts.remove(contact)
contact_manager=ContactManager()
contact1=contact("Priya Jadhav","9673839167","priya4@gmail.com","latur")
contact2=contact("ganesh","7262019320","ganesh@gmail.com","pune")
contact_manager.add_contact(contact1)
contact_manager.add_contact(contact2)
contact_manager.view_contact_list()
results=contact_manager.search_contact("Priya")
for result in results:
    print(f"name:{result.name},phone:{result.phone},email:{result.email}")
    new_contact=contact("Priya","23768136","uyu@gmail.com","65765gu")
    contact_manager.update_contact(contact1,new_contact)
    contact_manager.delete_contact(contact2)
