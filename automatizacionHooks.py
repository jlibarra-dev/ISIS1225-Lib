# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 11:52:36 2020

@author: juanl
"""

libreriasParaActualizar = ['ISIS1225-SampleTree', 'ISIS1225-SampleGraph']#, "Reto4-202020-Template"]
nombreRepositorio = "jlibarra-dev"
with open('.git/hooks/pre-push', 'w') as writer:
    # Further file processing goes here
    writer.write("#!/bin/sh\n")
    writer.write("cd ../\n")
    for i in libreriasParaActualizar:
        writer.write("git clone https://github.com/" + nombreRepositorio + "/" + i + ".git" + "\n")
        writer.write("cd " + i + "\n")
        writer.write("rm -rf DISClib\n")
        writer.write("cd ../\n")
        writer.write("cp -R ISIS1225-Lib/DISClib " + i + "\n")
        writer.write("cd " + i + "\n")
        writer.write("git add .\n")
        writer.write("git commit -m \"Cambios realizados desde ISIS1225-Lib\"\n")
        writer.write("git push\n")
        writer.write("cd ../\n")
        writer.write("rm -rf " + i + "\n")
    writer.close()

with open('.git/hooks/pre-push', 'r') as reader:
    # Further file processing goes here
    line = reader.readline()
    while line != '':
         print(line, end='')
         line = reader.readline()
    reader.close()
