#!/usr/bin/env python3
# coding: utf8

import time
import csv
import glob
import os
import bibtexparser


class smart_dict(dict):
    def __missing__(self, key):
        return ""

prefix = "vml-all"
suffix = ".csv"
list_of_files = glob.glob(prefix + "*" + suffix)
latest_file = max(list_of_files, key=os.path.getctime)

now = time.strftime('%Y%m%d-%H-%M-%S')

newCols = ["authors"]


with open(latest_file, newline='') as csvfile:
    # Read csv file
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    publications = []
    colnames = []
    modif = False
    for row in spamreader:
        if len(colnames) == 0:
            colnames = row
        else:
            publications.append(smart_dict())
            for k, v in zip(colnames, row):
                publications[-1][k] = v


    
    # read BibTeX file
    with open('citations-vml.bib') as bibtex_file:
        bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)
        
        entries = [p["bibtex"] for p in publications]
        
        nbBefore = len(bib_database.entries)
        
        bib_database.entries = [ e for e in bib_database.entries if e['ID'] in entries]
        
        nbAfter = len(bib_database.entries)

        if nbBefore != nbAfter:
            print ("Removing " + str(nbBefore - nbAfter) + " unused entries ("+ str(nbBefore) + " -> " + str(nbAfter) +")")
            with open('citations-vml-' + now + '.bib', 'w') as bibtex_file_out:
                bibtexparser.dump(bib_database, bibtex_file_out)
        else:
            print("No entry has been removed")
