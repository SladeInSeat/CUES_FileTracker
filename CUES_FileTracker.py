import os
import csv
import shutil



extension_locators = {'.JPG': r'J:\\GIS_Media\Photos',
                      '.mpg': r'J:\\GIS_Media\Video',
                      '.wmv': r'J:\\GIS_Media\Video',
                      '.gnet': r'J:\\GIS_Media\Fusion'}

exclude = {'GIS_Media'}
cwd = r"J:\\"
os.chdir(cwd)

with open(r"J:\Moved.csv","w") as copied,\
     open(r"J:\NotMoved.csv","w") as notcopied:
    csvWritercopied = csv.writer(copied)
    csvWriternotcopied = csv.writer(notcopied)
    for root, dirs, files in os.walk(cwd):
        dirs[:] = [d for d in dirs if d not in exclude]
        if len(files) > 0:
            for filename in files:
                file_path = "\\".join((root,filename))
                ext = os.path.splitext(file_path)[1]
                file_size = os.path.getsize(file_path)
                if ext in extension_locators.keys():
                    try:
                        shutil.move(file_path,extension_locators[ext])
                        csvWritercopied.writerow([file_path,filename,ext,file_size])
                        print "{} moved to {}".format(filename,root)
                    except shutil.Error as ShutilErr:
                        print ShutilErr.args
                        csvWriternotcopied.writerow([file_path,filename,ext,file_size,ShutilErr.args])
                    except TypeError as TypeErr:
                        print TypeErr.args
                        csvWriternotcopied.writerow([file_path, filename, ext, file_size,TypeErr.args])


