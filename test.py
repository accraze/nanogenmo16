import unittest
import re

from markov import MarkovModel

class TestMarkov(unittest.TestCase):

    def test_clean_sentences(self):
      # test single regex pattern
      regex = re.compile(r'[0-9]*^.*?\s[A-Z]*\s[A-Z]*')
      m = MarkovModel(exclude=regex)
      sentences = ['138 TEST STRING', 'second string is here']
      self.assertEquals(len(sentences), 2)
      cleaned = m._clean_sentences(sentences)
      self.assertEquals(len(cleaned), 1)

      # test list of regex patterns
      reg_list = [regex]
      regex2 = re.compile(r'[a-z]*\s[a-z]*\s[a-z]*\s[a-z]')
      reg_list.append(regex2)
      m = MarkovModel(exclude=reg_list)
      cleaned = m._clean_sentences(sentences)
      self.assertEquals(len(cleaned), 0)

if __name__ == '__main__':
    unittest.main()
