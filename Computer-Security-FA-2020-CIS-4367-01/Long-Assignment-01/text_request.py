import requests


def make_request(url):
    response = requests.get(url, headers={"User-Agent": ""})
    return response.status_code, response.text


class OnlineTextResource():
    """
    Class used to fetch a remote text file for testing and more analysis. Uses the `requests` library.
    """

    def __init__(self, url):
        self.status_code, self.text = make_request(url)
