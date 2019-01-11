import os
import csv
import collections

cwd = r"J:\\"
os.chdir(cwd)
extensions = set()
sp_dict = collections.defaultdict(list)
with open(r"J:\cues_files_allextensions.csv","w") as csvobj:
    csvWriter = csv.writer(csvobj)
    for root, dirs, files in os.walk(cwd):
        if len(files) > 0:
            for filename in files:
                file_path = "\\".join((root,filename))
                ext = os.path.splitext(file_path)[1]
                file_size = os.path.getsize(file_path)
                # if ext in ('.mpg','.wmv'):
                csvWriter.writerow([root, filename, ext, file_size])
#                 sp_dict[str(file_size)].append(file_path)
#
# with open(r"J:/duplicates_by_filesize.csv","w") as duplicates:
#     del_bool = None
#     csvWriter = csv.writer(duplicates)
#     for k,v in sp_dict.iteritems():
#         if len(v) > 1:
#             filenames = {os.path.split(filepath)[1] for filepath in v}
#             if len(filenames) == 1:
#                 del_bool = ['TRUE']
#             else:
#                 del_bool = ['FALSE']
#             csvWriter.writerow([k] + del_bool + v)

