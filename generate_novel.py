from markov import MarkovModel
from novel import Novel

m = MarkovModel()
m.train_model('FuturistManifesto')

novel = Novel(m.model, chapter_count=3)
novel.write(novel_title='mynovel')

