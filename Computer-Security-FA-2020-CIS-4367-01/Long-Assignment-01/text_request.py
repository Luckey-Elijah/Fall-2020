import requests


def make_request(url):
    response = requests.get(url, headers={"User-Agent": "XY"})
    return response.status_code, response.text


class OnlineText():
    """
    Class used to fetch a remote text file for testing and more analysis. Uses the `requests` library.
    """

    def __init__(self, url):
        self.status_code, self.text = make_request(url)
