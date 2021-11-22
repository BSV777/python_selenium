from model import Group


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="new NAME"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="new HEADER"))

