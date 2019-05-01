from datascience import *
from datascience.predicates import are
import numpy as np
import matplotlib
matplotlib.use('Agg', warn=False)
%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from urllib.request import urlopen
import re
def read_url(url):
    return re.sub('\\s+', ' ', urlopen(url).read().decode())

import pandas as pd
from typing import Union, List, Set
from tokenizer import tokenize
from typing import Dict
from collections import Counter

from IPython.display import Image
from IPython.core.display import HTML

# Tom Sawyer
TS_url = 'http://www.gutenberg.org/files/74/74-0.txt'
TS_text = read_url(TS_url)
TS_chapters = TS_text.split('CHAPTER')[36:]
Table().with_column('Tom Sawyer Chapters',TS_chapters)

# Huckleberry Finn
HF_url = 'http://www.gutenberg.org/files/76/76-0.txt'
HF_text = read_url(HF_url)
HF_chapters = HF_text.split('CHAPTER')[44:]
Table().with_column('Huckleburry Finn',HF_chapters)

# Tom Sawyer Sentence Length
wordcount=[s.count(" ") for s in TS_chapters]
periodcount=np.char.count(TS_chapters, '.')
exclamationcount=np.char.count(TS_chapters, '!')
questioncount=np.char.count(TS_chapters, '?')
SentenceNumber=periodcount+exclamationcount+questioncount

chars_periods_TS = Table().with_columns([
        'Tom Sawyer Chapter Length', wordcount,
        'Number of Sentences', SentenceNumber,
        'Sentence Length', wordcount/SentenceNumber])
chars_periods_TS

# Huckleberry Finn
wordcount=[s.count(" ") for s in HF_chapters]
periodcount=np.char.count(HF_chapters, '.')
exclamationcount=np.char.count(HF_chapters, '!')
questioncount=np.char.count(HF_chapters, '?')
SentenceNumber=periodcount+exclamationcount+questioncount

chars_periods_HF = Table().with_columns([
        'Huckberry Finn Chapter Length', wordcount,
        'Number of Sentences', SentenceNumber,
        'Sentence Length', wordcount/SentenceNumber])
chars_periods_HF

# Sentence Legnth Comparison Table
TSSummary=pd.DataFrame(chars_periods_TS["Sentence Length"]).describe()
HFSummary=pd.DataFrame(chars_periods_HF["Sentence Length"]).describe()
CombinedSummary=pd.concat([TSSummary,HFSummary], axis=1, join='inner')
CombinedSummary.columns=["Tom Sawyer","Huckleberry Finn"]
CombinedSummary.round(2)

# Distribution 
plots.figure(figsize=(10,5))
plots.subplot(1,2,1)
plots.hist(chars_periods_TS['Sentence Length'],alpha=0.6,color='orange');
plots.xlabel("Sentence Length of Tom Sawyer")
plots.ylabel("Number of Sentences")
plots.subplot(1,2,2)
plots.hist(chars_periods_HF['Sentence Length'],alpha=0.6,color='green');
plots.xlabel("Sentence Length of Huckleberry Finn")
plots.ylabel("Number of Chapters")
plots.suptitle('Setence Length Comparison between Tom Sawyer and Huckleberry Finn');