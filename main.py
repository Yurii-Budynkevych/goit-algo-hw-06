from collections import UserDict

class PhoneError(Exception):
    def __init__(self, message="not ok number"):
        self.message = message
        super().__init__(self.message)

class RecordNotFoundError(Exception):
    pass

class Field:
    def __init__(self, value: str):
        self.value = value
        
    def get_value (self) -> str:
        return str(self.value)

class Name(Field):
    def __init__(self, name: str):
        name = name.lower().capitalize() 
        super().__init__(name)    

class Phone(Field):
    def __init__(self, phone: str):
        if not phone.isdigit() or len(phone) != 10:
            raise PhoneError() 
        super().__init__(phone)    

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []

    def add_phone (self, phone: str) -> None:
        new_phone = Phone(phone) 
        self.phones.append(new_phone)

    def edit_phone (self, phone: str, edited_phone: str) -> None:
        for el in self.phones:
            if el.value == phone:
                el.value = edited_phone

    def find_phone (self, phone: str) -> str | None:
        for el in self.phones:
            if el.value == phone:
                return phone
        return None
    
    def remove_phone(self, phone: str) -> None:
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el)
                break 
    
    def get_value (self) -> str:
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name.get_value()] = record

    def find(self, record_name: str) -> Record | None:
        if record_name not in self.data:
            return None
        return self.data[record_name]
    
    def delete(self, record_name: str) -> None:
        self.data.pop(record_name) 



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("joHn")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
# Пайланс зходить з розуму через можливе Нан, тому додаю перевірку. Повертати Нан погана ідея!!!
john = book.find("John")
if john is not None:
    john.edit_phone("1234567890", "1112223333")
    print(john.get_value())
else:
    print("John not found")

# Пошук конкретного телефону у записі John
# Пайланс зходить з розуму через можливе Нан, тому додаю перевірку. Повертати Нан погана ідея!!!
if john is not None:
    found_phone = john.find_phone("1112223333")
    print(f"{john.name.value}: {found_phone}")
else:
    print("John not found")

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)