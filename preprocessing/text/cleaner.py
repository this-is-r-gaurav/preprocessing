from bs4 import BeautifulSoup
import re


class Cleaner(object):
    def __init__(self, org_text,):
        if isinstance(org_text, str):
            self.org_text = org_text
        else:
            raise TypeError("String Expected but {arg_type}".format(arg_type=type(org_text)))
        self.filtered_text = None

    def __str__(self):
        return self.filtered_text

    def clean_text(self):
        pass
