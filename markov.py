from internetarchive import download
import markovify
import glob
import nltk
import re
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
            self._create_markov(text)

    def _create_markov(self, text):
        """
        Assign markovify.Text 
        as model
        """
        self.model = markovify.Text(text)


class POSMarkov(MarkovModel):

    def _create_markov(self, text):
        """
        Assign part of speech tagged markov
        to model.
        """
        self.model = POSifiedText(text)


class POSifiedText(markovify.Text):
    """
    Override Markovify Text
    to use part-of-speech tagging
    on training text.
    """

    def word_split(self, sentence):
        words = re.split(self.word_split_pattern, sentence)
        print words
        try:
            words = ["::".join(tag) for tag in nltk.pos_tag(words)]
        except:
            pass
        return words

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence
