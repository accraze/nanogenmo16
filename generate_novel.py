from markov import MarkovModel, POSMarkov
import markovify
from markov_novel import Novel
import random

ia_archives = [
  'FuturistManifesto',
  'flatlandromanceo00abbouoft',
  'YouDontNeedAWeathermanToKnowWhichWayTheWindBlows_925',
  'btthg31.pdf',
  'al_FC_Industrial_Society_and_Its_Future_a4',
  'VaneigemTheRevolutionOfEverydayLife',
  'DebordSocietyOfTheSpectacleDonaldNicholsonSmithTranslation',
  'TheGeometry',
  'BurdenOfSkeptism-CarlSagan',
  'WallaceStevensTheNecessaryAngelEssaysOnRealityAndTheImagination',
  'arxiv-cs0007014',
  'al_Max_Cafard_The_Surre_gion_alist_Manifesto_and_Other_Writings_a4'
]

markov_models = []

for archive_name in ia_archives:
  m = POSMarkov()
  m.train_model(archive_name)
  markov_models.append(m.model)

# pick random weights for models
weights = []
for m in markov_models:
 weights.append(random.uniform(0.5, 2.0)) 

markov_combo = markovify.combine(markov_models, weights)

novel = Novel(markov_combo, chapter_count=10)
novel.write(novel_title='mynovel', filetype='md')

file = open('mynovel.md', 'r+')
word_count = 0
for word in file.read().split():
  word_count = word_count + 1
file.close()

print ('Total word count: %d' % word_count)


