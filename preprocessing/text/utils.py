from bs4 import BeautifulSoup
import re


class Utility(object):
    @classmethod
    def strip_html(cls, text):
        soup = BeautifulSoup(text, "html.parser")
        return soup.getText()

    @classmethod
    def strip_comments(cls, text):
        ml_c = re.compile("(\/\*{1,2}) | (\*{1,2}\/)")  # multi line commen /** **/
        sl_c = re.compile("(\/){2}")  # single line comment //
        html_c = re.compile("(<!-{2})|(-{2}>)")  # html comment // <!-- -->
        python_comments = re.compile("(#)")
        patterns = [html_c, sl_c, ml_c]
        for pattern in patterns:
            text = re.sub(pattern, "", text)
        return text

    @classmethod
    def strip_non_ascii(cls, text):
        if isinstance(text, str):
            temp = text
            temp = temp.encode('utf-8')
            temp = temp.decode('ascii', 'ignore')
            return temp
        else:
            raise TypeError(
                "Expected of type String, but org_text is of type {arg_type}".format(arg_type=type(text)))

    @classmethod
    def strip_duplicate_whitespaces(cls, text):
        sentence = " ".join(re.split("\s{2,}", text, flags=re.UNICODE))
        return sentence
