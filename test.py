import os

from argparse import ArgumentParser
from sys import argv
from sys import path
from sys import version_info
import os.path,subprocess
from subprocess import STDOUT,PIPE

from pipeline import Pipeline

if not version_info[0] < 3:
    from common.stanfordcorenlp.server import Server
    from facts_extractor.extractor import FactsExtractor
    from graph_generator.generator import GraphGenerator
    from kb_linker.linker import Linker
    from preprocessor.preprocessor import Preprocessor
    from rdf_maker.maker import RDFMaker

# text_file = open("sample.txt", "wt")
# n = text_file.write("Welcome to pythonexamples.org edit")
# text_file.close()


def run_kgen(file): #'/Users/kaifujimoto/Desktop/KGen/used_files/offprod_DatabaseSoftware.txt'
    pipeline = Pipeline()
    pipeline.run(file)

# #i can give it a direct path to cd into the java folder
# def compile_java(java_file):
#     subprocess.check_call(['javac', java_file])

# def execute_java(java_file, stdin):
#     java_class,ext = os.path.splitext(java_file)
#     cmd = ['java', java_class]
#     proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
#     stdout,stderr = proc.communicate(stdin)
#     print ('This was "' + stdout + '"')

# Context Manager to change current directory.
# I looked at this implementation on stackoverflow but unfortunately do not have the link
# to credit the user who wrote this part of the code.

#OWL API ______________________________________________
class changeDir:
  def __init__(self, newPath):
    self.newPath = os.path.expanduser(newPath)

  # Change directory with the new path
  def __enter__(self):
    self.savedPath = os.getcwd()
    os.chdir(self.newPath)

  # Return back to previous directory
  def __exit__(self, etype, value, traceback):
    os.chdir(self.savedPath)

filename = "./used_files/offprod_DatabaseSoftware.txt"

run_kgen(filename)

# folderPath = path of the folder you want to run mvn clean install on
with changeDir('/Users/kaifujimoto/Desktop/rdf_lib/my-app'):
  subprocess.call(["mvn", "install"])
  subprocess.call(["mvn", "exec:java", "-Dexec.mainClass=com.syrdec.app.App", "-Dexec.args=/Users/kaifujimoto/Desktop/KGen/used_files/offprod_DatabaseSoftware_preprocessed_kg.ttl databasesoftwarePLZ.owl"])

with changeDir('/Users/kaifujimoto/Desktop/logmap-matcher/target'):
    subprocess.call(["java", "-jar", "./logmap-matcher-3.0.jar", "MATCHER", "file:/Users/kaifujimoto/Desktop/rdf_lib/owlfiles/wordprocessing_software.owl", "file:/Users/kaifujimoto/Desktop/rdf_lib/my-app/databasesoftwarePLZ.owl", "TXT", "./output"])


# print(owl_api())
