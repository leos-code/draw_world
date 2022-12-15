from app.core.config import settings
import requests


import logging
# 启用调试于 http.client 级别 (requests->urllib3->http.client)
# 你将能看到 REQUEST，包括 HEADERS 和 DATA，以及包含 HEADERS 但不包含 DATA 的 RESPONSE。
# 唯一缺少的是 response.body，它不会被 log 记录。
try:
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection
HTTPConnection.debuglevel = 1

logging.basicConfig() # 初始化 logging，否则不会看到任何 requests 的输出。
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class ByteDance:
    
    def __init__(self, app_id:str, app_secret: str):
        self.app_id = app_id
        self.app_secret = app_secret
        self.base_url = "https://developer.toutiao.com/api"

    def code2Session(self, code: str):
        payload = {
            "appid": self.app_id,
            "secret": self.app_secret,
            "code": code.strip(),
            "anonymous_code":""
        }
        url = self.base_url + "/apps/v2/jscode2session"
        rsp = requests.post(url, json=payload)
        print("=======", rsp.status_code, rsp.json())
        return dotdict(rsp.json()["data"])


tt_app = ByteDance(
    # 核心配置
    app_id=settings.APP_ID,
    app_secret=settings.APP_SECRET
)

if __name__ == "__main__":
    code="""
    ES-J4NnMGkUdU1CKZKXm5vADV54jMhKlutxOP03SBAbhC2d6qUbdkdedVfcZCt84SDp2-W6CZFQl-EPzqug1u19vB1HCUrlbO5Y6XHkbDGoy0wZsWAyUoQFEn94
    """
    rsp = tt_app.code2Session(code)
    print("unionid:", rsp.unionid, rsp.openid)