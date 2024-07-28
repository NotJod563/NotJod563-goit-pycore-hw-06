from collections import UserDict
import re

class Field: # Базовий клас для полів запису
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field): # Клас для зберігання імені контакту. Обов'язкове поле.
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class Phone(Field): # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record: # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):  # Метод для додавання телефону до запису
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):  # Метод для видалення телефону з запису
        new_phones = []
        for phone in self.phones:
            if phone.value != phone:
                new_phones.append(phone)
        self.phones = new_phones

    def edit_phone(self, old_phone, new_phone):  # Метод для редагування телефону в записі
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def find_phone(self, phone): # Метод для пошуку телефону в записі
        for phone in self.phones:
            if phone.value == phone:
                return phone
        return None

    # Метод для представлення запису у вигляді рядка
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Клас для зберігання та управління записами
class AddressBook(UserDict):
    def add_record(self, record): # Метод для додавання запису до адресної книги
        self.data[record.name.value] = record

    def find(self, name): # Метод для пошуку запису за ім'ям
        return self.data.get(name, None)

    def delete(self, name): # Метод для видалення запису за ім'ям
        if name in self.data:
            del self.data[name]

# Приклад використання

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
