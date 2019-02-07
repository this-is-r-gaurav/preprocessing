import urllib.request as file_getter
import os
from tqdm import tqdm


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


class Downloader(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')

    @classmethod
    def download(cls, file_url, base_path: str = DATA_DIR):
        file = file_url.split('/')[-1]
        file_dir = file.split('.')[0]
        file_abs_dir = os.path.join(base_path, file_dir)
        if not os.path.exists(file_abs_dir):
            os.mkdir(file_abs_dir)
            file_abs_path = os.path.join(file_abs_dir, file)
            with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=file) as t:
                file_getter.urlretrieve(file_url, file_abs_path, reporthook=t.update_to)
            return file_abs_path
