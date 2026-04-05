#!/usr/bin/env python

import hrdweb as h
import misc
import os 

PHONY = ['./index.md']

for file, mtime in misc.get_all_files('.', 'md', reverse=False):
    mod_time = 0
    try:
        mod_time = os.stat(file.replace('md', 'html')).st_mtime
    except:
        pass
    if  mod_time < mtime or file in PHONY:
        print(f'Processing file: {file}...')
        h.convert(file)

print('Done')
