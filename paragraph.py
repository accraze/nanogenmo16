import markovify


class Paragraph(object):
    """
    Object to hold
    multiple setences created by
    a Markov Model
    """

    def __init__(self, model):
        if not isinstance(model, markovify.Text):
            raise Exception('model must be a markov model')
        self.model = model

    def get_paragrapgh(self):
        """
        Write a paragraph
        of 5 sentences.
        """
        self.text = ''
        for x in xrange(5):
            self.text = self.text + self.model.make_sentence()
        return self.text
