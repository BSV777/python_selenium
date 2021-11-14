from model import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="NAME", header="HEADER", footer="FOOTER"))
    app.session.logout()
