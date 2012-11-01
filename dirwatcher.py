#!/usr/bin/env python
# encoding: utf-8
"""
dirwatcher.py
A simple script to monitor if a directory is updated (a new file is added or removed)
Created by John Wesonga on 2012-10-28.

"""

import time
import os
import sys

def main(path_to_watch):
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(10)
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added: print "Added: ", ", ".join (added)
        if removed: print "Removed: ", ", ".join (removed)
        before = after
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        print sys.argv[-1]
        path = sys.argv[-1]
        main(path)
    else:
        print "Missing argument"
  

