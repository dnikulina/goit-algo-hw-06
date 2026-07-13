from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
		pass

class Phone(Field):
       def __init__(self, value): 
            if not value.isdigit() or len(value) != 10:
                   raise ValueError
            super().__init__(value)                          
    
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))  

    def find_phone(self, search_phone):
        for phone in self.phones:   
            if phone.value == search_phone:
                return phone
        return None

    def remove_phone(self, phone_to_remove):
        for phone in self.phones:
            if phone.value == phone_to_remove:
                self.phones.remove(phone)
                break    
    
    def edit_phone(self, old_phone, new_phone):
            validated_phone = Phone(new_phone)
            for phone in self.phones:
                if phone.value == old_phone:
                    phone.value = validated_phone.value
                return
            raise ValueError
     
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
        def add_record(self, record):
            self.data[record.name.value] = record

        def find(self, record_name):
            return self.data.get(record_name)

        def delete(self, record_to_delete):
            del self.data[record_to_delete]

        def __str__(self):
            return "\n".join(record.__str__() for record in self.data.values())    
          
          
    
		

book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    
book.add_record(john_record)

    
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

print(book)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")


book.delete("Jane")