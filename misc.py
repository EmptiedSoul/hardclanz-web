import os

def get_all_files(directory, filter_string, reverse):
    all_files = []

    for dirpath, dirs, files in os.walk('.'):
        if "__pycache__" in dirs:
            dirs.remove("__pycache__")
        for file in files:
            all_files.append((dirpath + '/' + file, os.stat(dirpath +'/'+ file).st_mtime))

    all_files.sort(key = lambda a: a[1], reverse=reverse)

    return list(filter(lambda x: filter_string in x[0], all_files))

def retrieve_header(fname):
    try:
        for line in open(fname, 'r').readlines():
            if line.startswith('#'):
                return line.strip('#').lstrip()
    except:
        pass
