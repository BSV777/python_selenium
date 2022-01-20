# -*- coding: utf-8 -*-
import allure
from model import Group
import pytest

#from data.add_group import testdata
#from data.groups import constant as testdata


#@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#def test_add_group(app, group):


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step('When I add a group %s to the list' % group):
        app.group.create(group)

    #assert len(old_groups) + 1 == app.group.count()

    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(app.group.get_group_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
