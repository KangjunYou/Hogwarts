# Jewish
# 2021/5/18 20:36
import json

import mitmproxy
from mitmproxy import http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            base_data = json.loads(flow.response.text)
            new_data = self.recursion(base_data,2)
            flow.response.text = json.dumps(new_data)

    def recursion(self,data,int_data):
        """
        :param data:原始的数据
        :return:在原始数据基础上，修改float类型，对float类型做数据翻倍操作
        """
        if isinstance(data, dict):
            # 如果是字典类型，继续递归value
            for k, v in data.items():
                data[k] = self.recursion(v,int_data)
        elif isinstance(data, list):
            # 递归算法，如果是list就继续遍历
            data_new = []
            for i in data:
                data_new.append(self.recursion(i,int_data))
        elif isinstance(data, float):
            data = data * int_data
        else:
            data = data
        return data

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', "-s", __file__])