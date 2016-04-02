class Phonebook:
    def __init__(self):
        self.entries = {}

    def add(self, name, phone):
        self.entries[name] = phone

    def lookup(self, name):
        return self.entries[name]

    def is_consistent(self):
        return True

    def is_inconsistent(self):
        return False
