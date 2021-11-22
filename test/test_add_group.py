# -*- coding: utf-8 -*-
from model import Group


def test_add_group(app):
    app.group.create(Group(name="GR.NAME", header="GR.HEADER", footer="GR.FOOTER"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


