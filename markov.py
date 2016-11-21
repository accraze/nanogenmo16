from internetarchive import download
import markovify
import glob
import os


class MarkovModel(object):

    """
    A Markov Model trained on
    on an Internet Archive text file.
    """

    def __init__(self):
        self.archive_name = None
        self.model = None

    def train_model(self, archive_name):
        """
        Trains the model
        on a given archive_name
        """
        self.archive_name = archive_name
        self._download_corpus()
        self._unpack_corpus()

    def _download_corpus(self):
        """
        Downloads a corpus of text
        from internet archive to 
        current working directory
        """
        download(self.archive_name, verbose=True, glob_pattern="*.txt")

    def _unpack_corpus(self):
        """
        unpacks a text file
        downloaded from internet archive
        """
        filenames = glob.glob(os.path.join(self.archive_name, '*.txt'))
        text = None
        for filename in filenames:
            with open(filename) as f:
                text = f.read()
            # build the model
            self.model = markovify.Text(text)
