# Jewish
# 2021/5/22 12:08
import json

import pytest

from Homework9_WeworkService.wework_api import WeWork


class TestWeWork:
    def setup_class(self):
        self.wework = WeWork()
        self.wework.get_token()

    def test_search(self):
        r = self.wework.search()
        assert r.json()['errcode'] == 0

    @pytest.mark.parametrize('group_name,tag_name', [["test0522_group1", "test1"]])
    def test_tag_add(self,group_name,tag_name):
        r = self.wework.add(group_name, tag_name)
        assert r.json()['errcode'] == 0
        r = self.wework.search()
        print(tag_name)
        assert tag_name in json.dumps(r.json())

    @pytest.mark.parametrize('tag_name', ["test"])
    def test_tag_delete(self,tag_name):
        tag_id = self.wework.get_tag_id(tag_name)
        r = self.wework.delete(tag_id)
        assert r.json()['errcode'] == 0
        r = self.wework.search()
        assert tag_name not in json.dumps(r.json())

    @pytest.mark.parametrize('old_tag_name,new_tag_name', [["test1", "test"]])
    def test_tag_edit(self,old_tag_name, new_tag_name):
        id = self.wework.get_tag_id(old_tag_name)
        print(id)
        r = self.wework.edit(id, new_tag_name)
        assert r.json()['errcode'] == 0
        r = self.wework.search()
        assert r.json()['errcode'] == 0
        assert new_tag_name in json.dumps(r.json())


