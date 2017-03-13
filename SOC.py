from BaseScraper import BaseScraper
from dialects import SOC_DIALECT

class SOC(BaseScraper):
    # Inline data representation or file name
    SITEMAP = 'sitemap.json'

    # GET OR POST
    HTTP_METHOD = 'POST'

    # If different data sets have different
    # URL's, map them here
    URL_PATHS = {
        'Aborter': 'if_abo',
        'Cancer': 'if_can'
    }

    DIALECT = SOC_DIALECT

    # Map the GET or POST parameters from the
    # standardized vocabulary to site specific names
    REQUESTS_PARAMS = {
        'distribution': 'vFOR',
        'region': 'hvOMR',
        'measure': 'vMATT',
        'year': 'vAR',
        'age': 'vAGI'
    }

    # For dynamic properties, create methods that
    # are accessible as properties of the scraper
    @property
    def BASE_URL(self):
        domain = 'http://sdb.socialstyrelsen.se'
        param = self.URL_PATHS[self.crt_label]
        return '{}/{}/resultat.aspx'.format(domain, param)


    def parse(self):
        """
        Parses the fetched HTML. Probably has to check
        what `label` we're dealing with to adjust the parser.
        """
        return self.html
