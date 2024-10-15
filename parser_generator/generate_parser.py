"""
The purpose of this program is just helping to generate a new parser (within this projects folder structure) with each change made to the contained grammar file.
"""

import sys
import os
import subprocess

# Pathing constants for this project
GRAMMAR_FILE = "SADATA.g4"
parser_generator_path = os.path.dirname(os.path.realpath(__file__))
grammar_path = os.path.join(parser_generator_path, GRAMMAR_FILE)
generated_parser_path = os.path.abspath(
    os.path.join(parser_generator_path, "..", "generated_parser")
)

# clear output path of generated product
os.chdir(generated_parser_path)
files = os.listdir()
for file in files:
    os.remove(file)

# set directory to parser generator
os.chdir(parser_generator_path)
curr_dir = os.getcwd()

# get files before parser generation (to track what has been generated)
orig_files_of_pg_dir = set(os.listdir())

# send command to generate parser
CLI = "cmd.exe"
commands = ["antlr4", "-Dlanguage=Python3", grammar_path]
output = subprocess.run(commands, shell=True, capture_output=True)
print(output)

# Track the files that have been generated
intermed_files_of_pg_dir = set(os.listdir())
generated_files = intermed_files_of_pg_dir - orig_files_of_pg_dir

# Move generated files to generated_parser folder
for file in generated_files:
    new_file_dest = os.path.join(generated_parser_path, file)
    os.rename(file, new_file_dest)
