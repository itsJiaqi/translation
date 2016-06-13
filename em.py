import numpy as np
from sklearn import mixture
import nltk
from nltk.corpus import wordnet

synon=wordnet.synsets('coffee')
print(synon)
synon=wordnet.synsets('bar')
print(synon)
