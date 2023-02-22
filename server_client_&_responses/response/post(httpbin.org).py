import requests


class Requests(object):

    def __init__(self, session: requests.session):

        self.session = session

    @staticmethod
    def requests(func):
        print(func.__name__)
        if func.__name__ == 'get':
            method = 'GET'

        def wrapper(*args, **kwargs):
            print(args[0].session)
            res = args[0].session.request(method=method, url=args[1], **kwargs)
            return res

        return wrapper

    @requests
    def get(self, url, **kwargs):
        pass


session = requests.session()
req = Requests(session)
res = req.get('https://httpbin.org/')
print(res.text)
