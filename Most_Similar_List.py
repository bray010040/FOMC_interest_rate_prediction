#Load Trained Model

import sys 
!{sys.executable} -m pip install Word2Vec
import sys 
!{sys.executable} -m pip install gensim
import gensim
import os
import pickle
w2v_file = os.path.join(os.getcwd(), "word_vectors.w2v")
model = gensim.models.Word2Vec.load(w2v_file)
  #Test whether vectors correctly loaded
  #print(model.wv.index2word)

##########

#Generate Most Similar List

import pprint as pp
  #This is Raise List
pp.pprint(model.wv.most_similar(positive=['raise'], negative = ['lower'], topn=500))
  #This is Lower List
pp.pprint(model.wv.most_similar(positive=['lower'], negative = ['raise'], topn=500))
