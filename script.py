import fileinput
from os import replace
import sys


files_list=[
    'tp1/tp1.tex',
    'tp2/tp2.tex',
    'tp3/tp3.tex',
    'tp4/tp4.tex',
    'tp5/tp5.tex',
    'tp6/tp6.tex',
    'tp7/tp7.tex',
    'tp8/tp8.tex',
    'tp9/tp9.tex',    
    'tp10/tp10.tex'
]
str1="version profesor"
str2="version alumnos"

str3='\\excludecomment{profesor}\n'

def replaceAll(file):
    for line in fileinput.input(file, inplace=1):
        if (str1 in line) or (str2 in line):
            line = str3
        sys.stdout.write(line)

for f in files_list:
    replaceAll(f)