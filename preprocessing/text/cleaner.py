from bs4 import BeautifulSoup
import re
from preprocessing.text.utils import Utility as TxtUtility


class Cleaner(object):
    def __init__(self, org_text, html=True, comments=True, non_ascii=True,
                 expand_contraction=False, dup_whitespace=True, w2d=True):
        """
        :param org_text: String, It contain the original Text Passed to the Cleaner
        :param html: Boolean, Whether to strip html tags or not
        :param comments: Boolean,Strip Comments Whether to strip comments in programming languages
        :param non_ascii: Boolean, Strip Non Ascii Character or Not
        :param expand_contraction:
        :param dup_whitespace:
        :param w2d:
        """
        if isinstance(org_text, str):
            self.org_text = org_text
        else:
            raise TypeError("String Expected but {arg_type}".format(arg_type=type(org_text)))
        self.html = html
        self.comments = comments
        self.non_ascii = non_ascii
        self.expand_contraction = expand_contraction
        self.dup_whitespace = dup_whitespace
        self.w2d = w2d
        self.filtered_text = self.clean_text()

    def __str__(self):
        return self.filtered_text

    def clean_text(self):
        temp = self.org_text
        if self.html:
            temp = TxtUtility.strip_html(temp)
        if self.comments:
            temp = TxtUtility.strip_comments(temp)
        if self.non_ascii:
            temp = TxtUtility.strip_comments(temp)
        if self.dup_whitespace:
            temp = TxtUtility.strip_duplicate_whitespaces(temp)
        if self.w2d:
            temp = TxtUtility.contract_word_to_digit(temp)
        if self.expand_contraction:
            temp = TxtUtility.strip_comments(temp)
        self.filtered_text = temp
        return temp
