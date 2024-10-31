import json
import os

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """Загружает контакты из JSON файла."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return {}

    def save_contacts(self):
        """Сохраняет контакты в JSON файл."""
        with open(self.filename, "w") as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email=""):
        """Добавляет новый контакт."""
        if name in self.contacts:
            print(f"Контакт с именем '{name}' уже существует.")
            return
        self.contacts[name] = {"phone": phone, "email": email}
        self.save_contacts()
        print(f"Контакт '{name}' добавлен.")

    def remove_contact(self, name):
        """Удаляет контакт по имени."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Контакт '{name}' удалён.")
        else:
            print(f"Контакт с именем '{name}' не найден.")

    def display_contacts(self):
        """Отображает все контакты."""
        if not self.contacts:
            print("Контактная книга пуста.")
        else:
            print("Контакты:")
            for name, details in self.contacts.items():
                print(f"Имя: {name}, Телефон: {details['phone']}, Email: {details['email']}")

    def find_contact(self, name):
        """Ищет контакт по имени."""
        contact = self.contacts.get(name)
        if contact:
            print(f"Имя: {name}, Телефон: {contact['phone']}, Email: {contact['email']}")
        else:
            print(f"Контакт с именем '{name}' не найден.")

def main():
    book = ContactBook()
    while True:
        print("\nКонтактная книга:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Показать все контакты")
        print("4. Найти контакт по имени")
        print("5. Выйти")

        choice = input("Выберите действие (1-5): ")
        
        if choice == "1":
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите email (необязательно): ")
            book.add_contact(name, phone, email)
        elif choice == "2":
            name = input("Введите имя контакта для удаления: ")
            book.remove_contact(name)
        elif choice == "3":
            book.display_contacts()
        elif choice == "4":
            name = input("Введите имя контакта для поиска: ")
            book.find_contact(name)
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == "__main__":
    main()
