# Jewish
# 2021/5/22 12:13
import json

import requests
from jsonpath import jsonpath


class WeWork:
    token=None
    def get_token(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={"corpid": "ww0174dd75bff3e33d",
                    "corpsecret": "apXSGeyYTj4CoPCHtifmsdMMIShAZpnU9oALaCmIF3E"
                    }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        self.token = r.json()['access_token']

    def search(self):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={"access_token": self.token},
            json={}
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def add(self, group_name, tag_name):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            params={"access_token": self.token},
            json={
                "group_name": group_name,
                "tag": [
                    {
                        "name": tag_name,
                    }
                ]
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def delete(self, tag_id):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag",
            params={"access_token": self.token},
            json={
                "tag_id": [
                    tag_id
                ]
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def edit(self, tag_id, tag_name):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            params={"access_token": self.token},
            json={
                "id": tag_id,
                "name" : tag_name,
            }
        )
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def get_tag_id(self, tag_name):
        r = self.search()
        group_list = r.json()['tag_group']
        for i in range(len(group_list)):
            tag_list = r.json()['tag_group'][i]['tag']
            for n in range(len(tag_list)):
                if r.json()['tag_group'][i]['tag'][n]['name'] == tag_name:
                    return r.json()['tag_group'][i]['tag'][n]['id']
