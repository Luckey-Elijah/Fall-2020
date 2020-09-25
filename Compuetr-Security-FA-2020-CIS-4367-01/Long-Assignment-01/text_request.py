import requests


def make_request(url):
    response = requests.get(url)
    response_code = response
    response_body = response.text
    return response_code, response_body


class OnlineResource():
    """
    Class used to fetch a remote text file for testing.
    """

    def __init__(self, url):
        self.code, self.text = make_request(url)
