# Summer-Project-2017
Contains my work at Brandeis in 2017 and related material

Details about software:

The code should run on using Python 3.5 32 bit and 32 bit nltk. I used 64 bit java 8 (i.e JDK 1.8) for supporting Stanford corenlp. Please refer: https://stanfordnlp.github.io/CoreNLP/ and look at https://stanfordnlp.github.io/CoreNLP/corenlp-server.html specifically. Note that 32 bit java will not work as there are memmory allocation issues while setting up the server. Also note that the nltk install, at least when I tried it, fails for most versions of python except for 3.5.


Basically the requirements for running most of the stuff I wrote or used are:


Download and install Python 3.5 (32 bit)

Download and install nltk (32 bit) (try https://pypi.python.org/pypi/nltk)

Download nltk data, in particular wordnet. To do this you can use the interactive installer. Just run the following in python:
>>import nltk
>>nltk.download()

Download and install Java 8 (64 bit) 

Download Stanford CoreNLP from https://stanfordnlp.github.io/CoreNLP/download.html

In your command line run:
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
 
