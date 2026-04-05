#!/usr/bin/env python

import hrdweb as h
import sys

h.convert(sys.argv[1], format='latex', output=open(sys.argv[1].replace('.md', '.latex'), 'w'))
