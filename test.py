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

def get_abspath_file(file):
    #returns the full path of the file in a string
    directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    filename = directory + '/output/' + file
    print(filename)

def run_kgen(file): #'/Users/kaifujimoto/Desktop/KGen/used_files/offprod_DatabaseSoftware.txt'
    pipeline = Pipeline()
    directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    filename = directory + '/output/' + file
    print(filename)
    abs_path_file = os.path.abspath(filename)
    print(abs_path_file)
    pipeline.run(abs_path_file)

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

filename = "output.txt"

run_kgen(filename)

def filename_without_ext(filename):
    return(os.path.splitext(filename)[0])

# print(filename_without_ext(filename))

# folderPath = path of the folder you want to run mvn clean install on
directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
owlapiPATH = directory + '/ttl_to_owl_converter'
# print(owlapiPATH)
with changeDir(owlapiPATH):
  subprocess.call(["mvn", "install"])
  directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
  file = filename_without_ext(filename)
  filename = directory + '/output/' + file + '_preprocessed_kg.ttl' + ' ' + directory + '/output/output.owl'
  print(filename)
  exec_filename = "-Dexec.args=" + filename
  print(exec_filename)
  subprocess.call(["mvn", "exec:java", "-Dexec.mainClass=com.syrdec.app.App", exec_filename])
#"-Dexec.args=/Users/kaifujimoto/Desktop/KGen/used_files/offprod_DatabaseSoftware_preprocessed_kg.ttl databasesoftwarePLZ.owl"
logmapPATH = directory + "/logmap-matcher/"
logmaptargetPATH = directory + "/logmap-matcher/target"
storedOnt = "/ontologies/wordprocessing_software.owl"

if not logmaptargetPATH:
    with changeDir(logmapPATH):
        subprocess.call(["mvn", "install"])


outputDir = directory + "/output/"
# directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
safireDir = os.path.abspath(os.path.join(os.getcwd(), "../.."))
print(safireDir)
with changeDir(logmapPATH):
    print(logmaptargetPATH)
    first_file = "file:" + safireDir + storedOnt
    second_file = "file:" + directory + "/output/output.owl"
    print(first_file)
    print(second_file)
    output_dir = directory + "/output/"
    subprocess.call(["java", "-jar", "./target/logmap-matcher-3.0.jar", "MATCHER", first_file, second_file, output_dir, "true"])
    # subprocess.call(["java", "-jar", "./logmap-matcher-3.0.jar", "MATCHER", "file:/Users/kaifujimoto/Desktop/rad/ui/satire-node-new/externals/temporary_ontologies/wordprocessing_software.owl", "file:/Users/kaifujimoto/Desktop/rad/ui/satire-node-new/externals/output/output.owl", "TXT", "./output"])



# print(owl_api())
