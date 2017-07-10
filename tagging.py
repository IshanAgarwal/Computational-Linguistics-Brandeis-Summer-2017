import nltk
from nltk.corpus import wordnet as wn
stuff=wn.synsets('object')[0]
hypostuff=set([i for i in stuff.closure(lambda s:s.hyponyms())])
hypo=set([])
artifacts=set([])
n=0
v=0

flag=0
length=0
a=list()
b=list()
c=list()
d=list()
glosses=list()
counter=0
stop=5000
for synset in list(wn.all_synsets('n')):
        stop=stop-1
        if stop<0:
                break
        hypo.clear()
        if(((synset.definition().count("used")>0)|(synset.definition().count("designed")>0))&(synset in hypostuff)):
               artifacts.add(synset)
               hypo=set([i for i in synset.closure(lambda s:s.hyponyms())])
               artifacts=artifacts.union(hypo)
    
    
        flag=0
        length=0
        counter=0
        n=0
        v=0
        while (counter<1):    
             counter=counter+1
             text=synset.definition()
             tokens=nltk.word_tokenize(text)
             this=nltk.pos_tag(tokens)
             length=len(this)-1
             
             for i in range(0,length):
                 
                if flag>0:
                     if ((this[i][1][0]=='N') & (n==0)):
                            a.append(this[i][0])
                            b.append(synset.lemmas()[0].name())
                            glosses.append(synset.definition())
                            n=1
                     if ((this[i][1][0]=='V') & (v==0)):
                            d.append(this[i][0])
                            v=1
                if this[i][0]=="used":
                        flag=1
             '''if flag!=1:
                 for i in range(0,length):

                     if flag>0:
                         if ((this[i][1][0]=='N') & (n==0)):
                                 a.append(this[i][0])
                                 b.append(synset.lemmas()[0].name())
                                 glosses.append(synset.definition())
                                 n=1
                         if ((this[i][1][0]=='V') & (v==0)):
                                 d.append(this[i][0])    
                                 v=1
                     if this[i][0]=="designed":
                          flag=1'''
             if ((v==0) & (flag>0)):
                    d.append("NF") 
             
c=list(zip(b,d,a))
out=list(zip(glosses,c))

target=open("parseout.txt","w")
for item in out:
        print(item)
        print("\n")
        


                                
        
        
