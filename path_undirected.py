from pycorenlp import StanfordCoreNLP
import json
nlp=StanfordCoreNLP('http://localhost:9000')
glosses=list()
trees=list()
file=open("output.txt","r")
target=open("parse.txt","w")
glosses=file.readlines()
count=1
next1="XXX"
next2="XXX"
next3="XXX"
for stuff in glosses:
     target.write("\n")
     target.write(stuff)
     target.write("\n")
     next1="XXX"
     next2="XXX"
     next3="XXX"
     
        
     out = nlp.annotate(stuff, properties={'annotators': 'tokenize,ssplit,pos,depparse,openie','outputFormat': 'json'})
     for item in out['sentences'][0]['basicDependencies']:
             if ((item['governorGloss']== "used")&(item['governor']<item['dependent'])):
                  next1=item['dependentGloss']
     for item in out['sentences'][0]['basicDependencies']:
             if item['governorGloss']== next1:
                  next2=item['dependentGloss']                  
     for item in out['sentences'][0]['basicDependencies']:
             if item['governorGloss']== next2:
                  next3=item['dependentGloss']

     count=count+1
     if next1!="XXX":
          target.write(next1)
          target.write("\n")
     if next2!="XXX":
          target.write(next2)
          target.write("\n")
     if next3!="XXX":
          target.write(next3)
          target.write("\n")

          
