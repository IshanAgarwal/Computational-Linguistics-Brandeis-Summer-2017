import nltk
from nltk.corpus import wordnet as wn

stuff=wn.synsets('object')[0]
hypostuff=set([i for i in stuff.closure(lambda s:s.hyponyms())])
hypo=set([])
artifacts=set([])
wn_artifacts=set([])
overlap=([])
wn_artifact = wn.synsets('artifact')[0]
wn_artifacts = set([i for i in wn_artifact.closure(lambda s:s.hyponyms())])

for synset in list(wn.all_synsets('n')):
        hypo.clear()
        if(((synset.definition().count("used")>0)|(synset.definition().count("designed")>0))&(synset in hypostuff)):
               artifacts.add(synset)
               hypo=set([i for i in synset.closure(lambda s:s.hyponyms())])
               artifacts=artifacts.union(hypo)

overlap= artifacts.intersection(wn_artifacts)
count_ours=len(artifacts)
count_theirs=len(wn_artifacts)
count_overlap=len(overlap)

precision=count_overlap/count_ours
recall=count_overlap/count_theirs

print(precision)
print(recall)
