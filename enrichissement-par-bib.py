import time
import csv
import glob
import os

prefix = "vml-all"
suffix = ".csv"
list_of_files = glob.glob(prefix + "*" + suffix)
latest_file = max(list_of_files, key=os.path.getctime)

now = time.strftime('%Y%m%d-%H-%M-%S')

with open(latest_file, newline='') as csvfile:
    # lecture du csv
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    publications = []
    colnames = []
    modif = True
    for row in spamreader:
        if len(colnames) == 0:
            colnames = row
        else:
            publications.append({})
            for k, v in zip(colnames, row):
                publications[-1][k] = v

    
    # sauvegarde du csv
    if modif:
        filename = prefix + "-" + now + suffix
        print("Écriture de " + filename)
        with open(filename, 'w', newline='') as wcsvfile:
            spamwriter = csv.writer(wcsvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(colnames)
            for p in publications:
                spamwriter.writerow([ p[h] for h in colnames])

    else:
        print("Aucune modification. Pas de sauvegarde")
