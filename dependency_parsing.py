from pycorenlp import StanfordCoreNLP
import json
nlp=StanfordCoreNLP('http://localhost:9000')
glosses=list()
trees=list()
file=open("output.txt","r")
target=open("trees.txt","w")
glosses=file.readlines()
count=1
for stuff in glosses:
     target.write(stuff)
     target.write("\n")
     if count%2==0:
        print("here")
        out = nlp.annotate(stuff, properties={'annotators': 'tokenize,ssplit,pos,depparse,openie','outputFormat': 'json'})
        for x in out['sentences'][0]['basicDependencies']:
            target.write(json.dumps(x,indent=4))
            target.write("\n")
        target.write("$\n")    
     count=count+1
    
target.close()
