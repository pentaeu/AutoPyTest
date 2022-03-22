from random import randrange
from model.contact import Contact
import re


def test_all_data_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="ContactName", lastname="ContactLastName", mobile_phone="+7934123455",
                                   work_phone="306312", home_phone="342321", email1="email1@test.com",
                                   email2="email2@test.com", email3="email3@test.com", address="test_street"))
    all_data_on_page_home = app.contact.get_contact_list()
    index = randrange(len(all_data_on_page_home))
    contact_data_from_home_page = all_data_on_page_home[index]
    contact_data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_data_from_home_page.id == contact_data_from_edit_page.id
    assert contact_data_from_home_page.lastname == contact_data_from_edit_page.lastname
    assert contact_data_from_home_page.firstname == contact_data_from_edit_page.firstname
    assert contact_data_from_home_page.address == contact_data_from_edit_page.address
    assert contact_data_from_home_page.all_emails_from_home_page == \
           merge_emails_on_edit_page(contact_data_from_edit_page)
    assert contact_data_from_home_page.all_phones_from_home_page == \
           merge_phones_on_edit_page(contact_data_from_edit_page)


def test_phones_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(mobile_phone="+79234234", work_phone="342345", home_phone="312345"))
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_on_edit_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(mobile_phone="+79234234", work_phone="342345", home_phone="312345"))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_on_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone]))))


def merge_emails_on_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))
