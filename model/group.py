class Group:

    def __init__(self, name=None, header=None, footer=None, group_id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s" % (self.group_id, self.name)

    def __eq__(self, other):
        return self.group_id == other.group_id and self.name == other.name
