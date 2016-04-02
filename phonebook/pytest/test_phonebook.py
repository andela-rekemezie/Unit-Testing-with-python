from phonebook import Phonebook
import pytest

#implementing fixtures in phonebook
@pytest.fixture
def phonebook(tmpdir):
    phonebook = Phonebook(tmpdir)
    return phonebook

# @phonebook.skip('WIP')
def test_look_up_user_name_in_the_phonebook(phonebook):
    phonebook.add('1234', 'Rowland')
    assert '1234' == phonebook.lookup('Rowland'), 'Rowland not found'

def test_phonebook_gives_access_to_the_list_of_numbers_and_phones(phonebook):
    phonebook.add('1234', 'Rowland')
    phonebook.add('2345', 'Alice')
    assert 'Rowland' in phonebook.names()
    assert '2345' in phonebook.phones()
    assert set(phonebook.names()) == {'Rowland', 'Alice'}


def test_raise_keyerror_for_invalid_key(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('missing')

# content of test_sample.py
# def func(x):
#     return x + 1
#
# def test_answer():
#     assert func(3) == 4