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

# Tokenization Function
def tok(text: str, flag: int = 2) -> Union[List[str], Set[str], Dict[str, int]]:
    return Counter([t.txt for t in tokenize(text) if t.txt])

# Most Frequent Word in TS
TS = tok(TS_text)
temp = {}
for k, v in sorted(TS.items(), key=lambda x: x[1], reverse=True)[:30]:
    temp[k] = v

plots.figure(figsize=(20, 7))
plots.bar(range(len(temp)), list(temp.values()), align='center')
plots.xticks(range(len(temp)), list(temp.keys()))
plots.xlabel("Word and Special Character in Tom Sawyer")
plots.ylabel("Appearance Frequency")
plots.show()

# Most Frequent Word in HF
HF = tok(HF_text)
temp = {}
for k, v in sorted(HF.items(), key=lambda x: x[1], reverse=True)[:30]:
    temp[k] = v

plots.figure(figsize=(20, 7))
plots.bar(range(len(temp)), list(temp.values()), align='center', color='green')
plots.xticks(range(len(temp)), list(temp.keys()))
plots.xlabel("Word and Special Character in Huckleberry Finn")
plots.ylabel("Appearance Frequency")
plots.show()

# List Building
TS_List = []
for i in TS.items():
    TS_List.append(i[0])

HF_List = []
for i in HF.items():
    HF_List.append(i[0])

# Building Charts
HF_Only = {}
for i in HF.items():
    if i[0] not in TS_List:
        HF_Only[i[0]] = i[1]

temp = {}
for k, v in sorted(HF_Only.items(), key=lambda x: x[1], reverse=True)[:20]:
    temp[k] = v

plots.figure(figsize=(20, 5))
plots.bar(range(len(temp)), list(temp.values()), align='center', color='orange')
plots.xticks(range(len(temp)), list(temp.keys()))
plots.xlabel("Huckleberry Finn Unique Word")
plots.ylabel("Appearance Frequency")
plots.show()