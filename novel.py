from chapter import Chapter


class Novel(object):
    """
    Writes a bunch of
    Chapters to file
    """

    def __init__(self, markov, chapter_count=1):
        self.chapters = []
        self.markov = markov
        self.chapter_count = chapter_count

    def write(self):
        self._compose_chapters()
        self._write_to_file()

    def _compose_chapters(self):
        """
        Creates a chapters
        and appends them to list
        """
        for count in xrange(self.chapter_count):
            c = Chapter(self.markov, count)
            self.chapters.append(c)

    def _write_to_file(self):
        with open('novel.txt', 'w') as f:
            for chapter in self.chapters:
                f.write(chapter.title)
                paragraphs = chapter.write_chapter()
                for paragraph in paragraphs:
                    f.write(paragraph)
