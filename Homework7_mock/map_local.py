# Jewish
# 2021/5/18 20:30
import mitmproxy
from mitmproxy import http

class Events:

    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        #匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            with open("quote.json",encoding="utf-8") as f:
                flow.response = http.HTTPResponse.make(
                    # 状态码
                    200,
                    # 响应体，传入数据格式为str
                    f.read(),
                    # 响应头
                )


    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        pass

addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-p', '8080', "-s", __file__])