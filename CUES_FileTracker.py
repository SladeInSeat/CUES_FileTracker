import os
import csv

cwd = r"J:\GraniteNet"
os.chdir(cwd)
with open(r"J:\changedit.csv","w") as csvobj:
    csvWriter = csv.writer(csvobj)
    for root, dirs, files in os.walk(cwd):
        if len(files) > 0:
            for filename in files:
                file_path = "\\".join((root,filename))
                ext = os.path.splitext(file_path)[1]
                if ext == '.mdb':
                    csvWriter.writerow([root, filename])

