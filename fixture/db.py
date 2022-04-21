import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return group_list

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2,"
                           " email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                contact_list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                            home_phone=home, mobile_phone=mobile, work_phone=work,
                                            email1=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return contact_list

    def add_contact_to_group_by_id(self, contact_id, group_id):
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"INSERT INTO `address_in_groups` (`domain_id`, `id`, `group_id`, `created`, `modified`, `deprecated`) VALUES "
                           f"('0', '{contact_id}', '{group_id}', '2022-04-10 00:00:00', '2022-04-10 00:00:00', '0000-00-00 00:00:00')")
        finally:
            cursor.close()

    def get_groups_with_contacts(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from address_in_groups")
            for group_id in cursor:
                (id,) = group_id
                group_list.append(str(id))
        finally:
            cursor.close()
        return group_list

    def destroy(self):
        self.connection.close()
