import unittest
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

    # Setup fixture
    def setUp(self):
        self.phonebook = Phonebook()

    def test_lookup_user_name(self):
        self.phonebook.add('Rowland', '23444')
        self.assertEquals('23444', self.phonebook.lookup('Rowland'))

    def test_missing_key_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    # @unittest.skip('WIP')
    def test_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_normal_entries_to_the_phonebook_is_consistent(self):
        self.phonebook.add('Ekemezie', '3453')
        self.assertTrue(self.phonebook.is_consistent())

    def test_duplicate_entries_to_the_phonebook_is_inconsistent(self):
        self.phonebook.add('Emma', '123')
        self.phonebook.add('Eke', '123')
        self.assertFalse(self.phonebook.is_inconsistent())

    def test_same_prefix_entries_to_the_phonebook_is_inconsistent(self):
        self.phonebook.add('Emma', '123455')
        self.phonebook.add('Eke', '12')
        self.assertFalse(self.phonebook.is_inconsistent())
