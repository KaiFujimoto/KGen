# KGen
Knowledge graphs generation from unstructured text

usage: python3 pipeline.py -f text.txt

# Windows integration notes
Python 3.7 virtual environment

Installed SENNA v3.0 and set environment variable SENNA_DIR 
to 'D:\dev\senna-v3.0\senna\'

Updated babelfy and NCBO BioPortal keys

pip install requests nltk stanfordcorenlp scispacy

Ran CoreNLP server separately:
java -mx8g edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 30000

Not working yet:
- Local initiation of CoreNLP server
- Filename checks
- Simplifier disabled
- Graphing (rapper will probably not work in Windows)
- babelfy.py copied into project to make it work

