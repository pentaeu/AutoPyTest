from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None,
                 company=None, address=None, email1=None, email2=None, email3=None, id=None, mobile_phone=None,
                 home_phone=None, work_phone=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.home_phone = home_phone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % \
                        (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.title,
                         self.company, self.address, self.email1, self.email2, self.email3, self.mobile_phone,
                         self.work_phone, self.home_phone, self.all_emails_from_home_page,
                         self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname \
               and self.middlename == other.middlename and self.nickname == other.nickname \
               and self.title == other.title and self.company == other.company and self.address == other.address \
               and self.email1 == other.email1 and self.email2 == other.email2 and self.email3 == other.email3 \
               and self.mobile_phone == other.mobile_phone and self.work_phone == other.work_phone \
               and self.home_phone == other.home_phone \
               and self.all_emails_from_home_page == other.all_emails_from_home_page \
               and self.all_phones_from_home_page == other.all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
