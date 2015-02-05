# -*- coding: utf-8 -*-
"""
Quickly evaluates performance of NTLK English stemmers on a word

Stemming is process of removing morphological affixes from words.
Below function returns stems per NLTK stemmers for quick perf. evaluation.

@author: CORAKWUE
"""

from tabulate import tabulate

#from nltk.stem.regexp import RegexpStemmer
from nltk.stem.lancaster import LancasterStemmer
#from nltk.stem.isri import ISRIStemmer [Arabic]
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
#from nltk.stem.rslp import RSLPStemmer [Portugese]
from modified_porter_stemmer import ModifiedPorterStemmer
from nltk.corpus import words
from random import randint


# Compare performance for below hand-picked words
tokens = ['elaborates', 'activate', 'critically', 'substituting', 'learning', 'educating',
         'creation','braille', 'security', 'business', 'tenderness', 'tabulate', 'connections', 'relativity']

tokens += ['geography', 'unseparable', 'beauty', 'beautiful', 'ability',
          'interpilastering', 'interplanetary',
          'gluttingly', 'especially', 'psychobiology', 
          'magical', 'magically', 'adulatory', 'mandatory'  ]

tokens += ['microchemistry', 'scorningly', 'excystate', 'execrable', 'statued', 'statuary',
          'sparringly']

## or compare with random bag of words

#random_range =  randint(0, 236736)
#
#tokens = words.words()[random_range-10:random_range]

wnl = WordNetLemmatizer()
wnl.stem = wnl.lemmatize

STEMMERS = {
#    'Regexp': RegexpStemmer(regexp=),
    'Lancaster': LancasterStemmer(),
    'Porter': PorterStemmer(),
    'Modified-Porter': ModifiedPorterStemmer(),
    'Snowball-EN': SnowballStemmer('english'),
    'WordNet-Lemma': wnl,
}


table_headers =  ["Word/Stemmer"] + STEMMERS.keys()

table = []
for t in tokens:
    result = [t]
    table.append(result + [stemmer.stem(t) for stemmer in STEMMERS.values()])
    
print tabulate(table, headers=table_headers, tablefmt="orgtbl")

#Modifief Porter Evalaution
#
#mps = ModifiedPorterStemmer(verbose=True)
#
#for t in tokens:
#    print "ModifiedPorterStemmer: Evaluating {}".format(t)
#    print mps.stem(t)