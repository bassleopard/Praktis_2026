class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class PhoneBook:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    # Власна хеш-функція
    def _hash(self, key):
        hash_value = 0

        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity

        return hash_value

    # Додавання контакту
    def add(self, name, phone):
        index = self._hash(name)
        current = self.table[index]

        # Оновлення існуючого контакту
        while current:
            if current.key == name:
                current.value = phone
                return
            current = current.next

        # Додавання нового вузла
        new_node = Node(name, phone)
        new_node.next = self.table[index]
        self.table[index] = new_node

        self.size += 1

        # Перевірка коефіцієнта заповнення
        if self.size / self.capacity > 0.75:
            self._resize()

    # Отримання номера
    def get(self, name):
        index = self._hash(name)
        current = self.table[index]

        while current:
            if current.key == name:
                return current.value
            current = current.next

        return None

    # Видалення контакту
    def remove(self, name):
        index = self._hash(name)
        current = self.table[index]
        prev = None

        while current:
            if current.key == name:

                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next

                self.size -= 1
                return True

            prev = current
            current = current.next

        return False

    # Перевірка наявності
    def contains(self, name):
        return self.get(name) is not None

    # Кількість контактів
    def count(self):
        return self.size

    # Розширення таблиці
    def _resize(self):
        old_table = self.table

        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for head in old_table:
            current = head

            while current:
                self.add(current.key, current.value)
                current = current.next


# Приклад використання
phone_book = PhoneBook()

phone_book.add("Ivan", "+380111111111")
phone_book.add("Olena", "+380222222222")
phone_book.add("Petro", "+380333333333")

print(phone_book.get("Olena"))

print(phone_book.contains("Ivan"))

phone_book.remove("Petro")

print(phone_book.count())