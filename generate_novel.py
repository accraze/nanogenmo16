import markovify
from markov_novel import Novel
from ia_markov import MarkovModel, POSMarkov
import random
import re

import time 
startTime = time.time()


ia_archives = [
  ('FuturistManifesto', None),
  ('flatlandromanceo00abbouoft', None),
  ('YouDontNeedAWeathermanToKnowWhichWayTheWindBlows_925', None),
  ('btthg31.pdf', None),
  ('al_FC_Industrial_Society_and_Its_Future_a4',None),
  ('VaneigemTheRevolutionOfEverydayLife', 
      [
        re.compile(r'/[0-9]*^.*?\s[A-Z]*\s[A-Z]*/'),
        re.compile(r'/[0-9]*^.*?\s[A-Z]*\s[A-Z]*\s[A-Z]*\s[A-Z]*\s[A-Z]*[0-9]*/')
      ]
  ),
  ('DebordSocietyOfTheSpectacleDonaldNicholsonSmithTranslation',
      re.compile(r'/[0-9]*^.*?\s[A-Z]*\s[A-Z]*\s[A-Z]*\s[A-Z]*\s[A-Z]*/')
  ),
  ('TheGeometry',None),
  ('BurdenOfSkeptism-CarlSagan', None),
  ('WallaceStevensTheNecessaryAngelEssaysOnRealityAndTheImagination', None),
  ('arxiv-cs0007014', None),
  ('al_Max_Cafard_The_Surre_gion_alist_Manifesto_and_Other_Writings_a4', None)
]

markov_models = []

for archive_name, excludes in ia_archives:
  m = POSMarkov(exclude=excludes)
  m.train_model(archive_name)
  markov_models.append(m.model)

# pick random weights for models
weights = []
for m in markov_models:
 weights.append(random.uniform(0.5, 2.0)) 

markov_combo = markovify.combine(markov_models, weights)

novel = Novel(markov_combo, chapter_count=2)
novel.write(novel_title='mynovel2', filetype='md')

file = open('mynovel.md', 'r+')
word_count = 0
for word in file.read().split():
  word_count = word_count + 1
file.close()

print ''
print '*** NOVEL COMPLETED ***'
print ('Total runtime: {0} secs'.format(time.time() - startTime))
print ('Total word count: %d' % word_count)


