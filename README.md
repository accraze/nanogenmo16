# nanogenmo16
A post-geometric futurist manifesto

Still work in progress

## Usage

How to write a chapter:

```
from markov import MarkovModel
from chapter import Chapter

# create a markov model with text
# from internet archive
m = MarkovModel()
m.train_model('FuturistManifesto')

# write a chapter with markov model
c = Chapter(m.model)
c.write_chapter()
```
