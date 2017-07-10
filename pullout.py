import nltk
from nltk.corpus import wordnet as wn
stuff=wn.synsets('object')[0]
hypostuff=set([i for i in stuff.closure(lambda s:s.hyponyms())])
hypo=set([])
target=open("output.txt","w")
for synset in list(wn.all_synsets('n')):
     if(((synset.definition().count("used")>0)|(synset.definition().count("designed")>0))&(synset in hypostuff)):
          target.write(synset.lemmas()[0].name())
          target.write("\n")
          target.write(synset.definition())
          target.write("\n")
target.close()          
