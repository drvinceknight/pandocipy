#!/usr/bin/env python
"""
pandocipy - create html, pdf, and docx versions of all md files in a directory

Usage: pandocipy
       pandocipy  -i FILES TO IGNORE

By Vincent Knight (www.vincent-knight.com)
License: BSD, see LICENSE for more details.
"""
import os
import sys


arguments = sys.argv[1:]  # Read in passed options

# Finding files to ignore
files_to_ignore = ""
if '-i' in arguments:
    ipos = arguments.index('-i')
    files_to_ignore = arguments[ipos + 1:]

directory = "./"
if len(arguments) > 0 and arguments[0] != "-i":
    directory += arguments[0]

markdown_files = [e[:-3] for e in os.listdir(directory) if ".md" in e]
for e in markdown_files:
    if e in files_to_ignore:
        markdown_files.remove(e)

for e in markdown_files:
    print "\nWorking on ", e
    os.system("pandoc " + directory + e + ".md -o " + directory + e + ".pdf")
    print "\t %s.pdf created" % e
    os.system("pandoc " + directory + e + ".md -o " + directory + e + ".html --webtex")
    print "\t %s.html created" % e
    os.system("pandoc " + directory + e + ".md -o " + directory + e + ".docx")
    print "\t %s.docx created" % e
