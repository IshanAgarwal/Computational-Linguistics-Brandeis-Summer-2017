import nltk
from nltk.corpus import wordnet as wn
from pycorenlp import StanfordCoreNLP
import json
nlp=StanfordCoreNLP('http://localhost:9000')
glosses=list()
trees=list()
target=open("parsed_run.txt","w")
p=""
tokens=[["advcl","dobj", "amod"],["advcl","dobj"],["nmod","amod"]]
chk=1
start="used"

st=wn.synsets('object')[0]
hypostuff=set([i for i in st.closure(lambda s:s.hyponyms())])
hypo=set([])
for synset in list(wn.all_synsets('n')):
     p=""
     if(((synset.definition().count("used")>0)|(synset.definition().count("designed")>0))&(synset in hypostuff)):
          target.write("\n")
          target.write(synset.lemmas()[0].name())
          target.write("\n")
          target.write("\n")
          target.write(synset.definition())
          target.write("\n")
          start="used"
    
          stuff= synset.definition()      
          out = nlp.annotate(stuff, properties={'annotators': 'tokenize,ssplit,pos,depparse,openie','outputFormat': 'json'})
          for toke in tokens:
              p=""
              for tok in toke:

                   for item in out['sentences'][0]['basicDependencies']:
                       if ((item['governorGloss']==start) & (item['dep']==tok)):
                            if((item['governor']>item['dependent'])&(start== "used")):
                                 continue
                            p=p+start+" "
                            start=item['dependentGloss']
                   target.write(p)
                   target.write("\n")
