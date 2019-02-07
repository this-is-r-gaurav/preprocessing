from bs4 import BeautifulSoup
import re
from pycontractions import Contractions
import shutil
import os
from word2number import w2n
from preprocessing.utils.utility import Downloader
from preprocessing.constants import MINIFIED_CONTRACTIONS_DATA_URL as MCD, CONTRACTIONS_DATA_URL as CD
from gensim.scripts.glove2word2vec import glove2word2vec

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONT_DATA_PATH = os.path.join(BASE_DIR, 'data', 'GoogleNews-vectors-negative300',
                              'GoogleNews-vectors-negative300.bin.gz')
MINIFIED_ZIP_CONT_DATA_PATH = os.path.join(BASE_DIR, 'data', 'word2vec_sample', 'word2vec_sample.zip')
MINIFIED_BIN_CONT_DATA_PATH = os.path.join(BASE_DIR, 'data', 'word2vec_sample', 'word2vec_sample.bin.gz')


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
        py_c = re.compile("(#)")
        patterns = [html_c, sl_c, ml_c, py_c]
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
    def strip_duplicate_whitespaces(cls, text: str):
        sentence = " ".join(re.split("\s{2,}", text, flags=re.UNICODE))
        return sentence

    @classmethod
    def expand_contractions(cls, text: str, minified_model=True):
        path = None
        url = None
        if minified_model == True:
            path = MINIFIED_BIN_CONT_DATA_PATH
            url = MCD
        else:
            path = CONT_DATA_PATH
            url = CD
        if not os.path.exists(path):
            cls.download_word_2_vec_model(url)
        ctr = Contractions(w2v_path=path)
        ctr.load_models()
        temp = list(ctr.expand_texts([text]))
        return temp[0]

    @classmethod
    def contract_word_to_digit(cls, text: str):
        sample = text.split()
        for i in range(len(sample)):
            try:
                word = w2n.word_to_num(sample[i])
            except ValueError:
                pass
            else:
                sample[i] = str(word)
        return " ".join(sample)

    @classmethod
    def download_word_2_vec_model(cls, file_url, minified_file=True):
        # Downloader.download(file_url)
        if minified_file:
            tmp_path = "/".join(MINIFIED_ZIP_CONT_DATA_PATH.split('/')[:-1])
            glove2word2vec(MINIFIED_ZIP_CONT_DATA_PATH, MINIFIED_BIN_CONT_DATA_PATH)
            shutil.rmtree()
            print(tmp_path)

