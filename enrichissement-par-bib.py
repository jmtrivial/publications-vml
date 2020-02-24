#!/usr/bin/env python3
# coding: utf8

import time
import csv
import glob
import os
import bibtexparser
import sys


class smart_dict(dict):
    def __missing__(self, key):
        return ""

prefix = "vml-all"
suffix = ".csv"
list_of_files = glob.glob(prefix + "*" + suffix)
latest_file = max(list_of_files, key=os.path.getctime)

now = time.strftime('%Y%m%d-%H-%M-%S')

newCols = ["authors"]

sortedEntries = ["title", "year", "type", "authors", "type", "num_citations", "bibtex", "url", "url_pdf", "url_versions", "excerpt"]


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

    # add possible missing headers
    for nc in newCols:
        if not nc in colnames:
            colnames.append(nc)
            modif = True

    # if a filtering is required as parameter
    if len(sys.argv) > 1 and sys.argv[1] == "--filter":
        print("Filtering columns")
        colnames = sortedEntries
    
    # read BibTeX file
    with open('citations-vml.bib') as bibtex_file:
        bib_database = bibtexparser.bparser.BibTexParser(common_strings=True).parse_file(bibtex_file)
        
        for p in publications:
            bib = [ b for b in bib_database.entries if b['ID'] == p["bibtex"] ]
            if len(bib) == 1 and "author" in bib[0]:
                p["authors"] = bib[0]["author"]
                modif = True

    # display some stats
    print("Total number of entries: " + str(len(publications)))
    print("Number of entries with author(s): " + str(len([p for p in publications if "authors" in p and p["authors"] != ""])))
    
    # save csv file
    if modif:
        filename = prefix + "-" + now + suffix
        print("Écriture de " + filename)
        with open(filename, 'w', newline='') as wcsvfile:
            spamwriter = csv.writer(wcsvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            spamwriter.writerow(colnames)
            for p in publications:
                spamwriter.writerow([ p[h] for h in colnames])

    else:
        print("Aucune modification. Pas de sauvegarde")
