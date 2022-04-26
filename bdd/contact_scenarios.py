from pytest_bdd import scenario
from .contacts_steps import *


@scenario('contacts.feature', 'Add new contact')
def test_add_new_contact():
    pass


@scenario('contacts.feature', 'Delete a contact')
def test_delete_contact():
    pass


@scenario('contacts.feature', 'Update a contact')
def test_update_contact():
    pass
