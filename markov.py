from internetarchive import download
import markovify
import glob
import os

ia_corpus_names = [
    'flatlandromanceo00abbouoft',
    'YouDontNeedAWeathermanToKnowWhichWayTheWindBlows_925',
    'FuturistManifesto',
    'TheSilverPanthersOfLunaAVisualCompanion',
    'btthg31.pdf',
    'al_FC_Industrial_Society_and_Its_Future_a4'
]




class MarkovModel(object):
  
  def __init__(self, archive_name):
      self.archive_name = archive_name
      self.model = None

  def train_model(self):
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
