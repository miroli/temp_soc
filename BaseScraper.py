import json
import requests
from builtins import filter  # python 2

class BaseScraper():
    """
    This scraper is messy, but serves the purpose of
    outlining the separation of concerns between the
    base scraper and the scraper implementations.
    """
    def list(self):
        """
        Lists all topics/data sets at the current level.
        """
        pass

    def get(self, label):
        """
        Selects a certain topic or data set by label.
        How to hand the user the sub topics while retaining
        chainability and returning self?
        """
        self.crt_label = label
        data = next(filter(lambda x: x['name'] == label, self._sitemap))
        # print(data)
        return self

    def fetch(self, data):
        """
        Fetches the actual data.
        """
        r = requests.request(self.HTTP_METHOD,
                             self.BASE_URL,
                             data=self._convert_params(data))
        self.html = r.text
        return self.parse()

    def _convert_params(self, params):
        """
        Converts the user paramaters to their site specific names.
        """
        converted = {}
        for key, val in params.items():
            new_key = self.REQUESTS_PARAMS.get(key, None)
            new_val = self.DIALECT[val]
            converted[new_key] = new_val
        return tuple(converted.items())

    @property
    def _sitemap(self):
        """
        Reads and caches the sitemap if it's an external file.
        """
        if type(self.SITEMAP) is str:
            with open(self.SITEMAP, 'r') as f:
                self.SITEMAP = json.loads(f.read())
        return self.SITEMAP
