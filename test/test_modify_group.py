from model import Group
import random

def test_modify_some_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups =db.get_group_list()

    group = random.choice(old_groups)

    #index = randrange(len(old_groups))

    #group = Group(name="new NAME")
    group.name = "new NAME"
    #group.id = old_groups[index].id

    app.group.modify_group_by_id(group.id, group)
    #assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()

    for g in old_groups:
        if g.id == group.id:
            g = group
            break

    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="new HEADER"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)

