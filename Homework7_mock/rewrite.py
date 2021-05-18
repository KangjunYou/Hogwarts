# Jewish
# 2021/5/17 22:18
"""HTTP-specific events."""
import json

import mitmproxy.http


class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        #匹配规则

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            data = json.loads(flow.response.text)
            #修改数据
            data["data"]["items"][0]["quote"]["name"] = "幕友"
            data["data"]["items"][1]["quote"]["name"] = "陆叁伍"
            data["data"]["items"][2]["quote"]["name"] = "Jewish"
            data["data"]["items"][0]["quote"]["percent"] = "0.01"
            data["data"]["items"][1]["quote"]["percent"] = "0.00"
            data["data"]["items"][2]["quote"]["percent"] = "-0.02"
            #修改响应
            flow.response.text = json.dumps(data)
addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', "-s", __file__])
