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

    # add possible missing headers
    for nc in newCols:
        if not nc in colnames:
            colnames.append(nc)
            modif = True

    
    # read BibTeX file
    # TODO

    
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
