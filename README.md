# Pandocipy

Working on a higher education certification process I've had to take a careful look at inclusivity of teaching resources. As a mathematician I always thought that there was not much more that could be done then a LaTeX and pdfs. Importantly, some students would like and/or need teaching resources (notes, exercise sheets etc) in different formats that would allow them to change formatting to make things easier to read.

[Pandoc](http://johnmacfarlane.net/pandoc/) is a great tool that allows you to go from one format to multiple others. It works great and often surprises me with how it never goes wrong.

![Using Pandoc for Universal Notes](https://docs.google.com/drawings/d/1sVRPkx7yr4smkZjb85DXF9UvvzDHNqS-1P4m9RXnVNQ/pub?w=867&h=396)

Importantly one can use LaTeX in the markdown file and this will still work.

This directory contains a simple python script that will take all markdown files in a directory and convert them to the following formats:

- html (using webtex which converts mathematics to image files);
- pdf (using LaTeX);
- docx.

# Usage

    pandocipy.py [Target Directory]
    pandocipy.py [Target Directory] -i [List of File to Ignore]

# License Information
This work is licensed under a [Creative Commons Attribution-ShareAlike 3.0](http://creativecommons.org/licenses/by-sa/3.0/us/) license.  You are free to:

* Share: copy, distribute, and transmit the work,
* Remix: adapt the work

Under the following conditions:

* Attribution: You must attribute the work in the manner specified by the author or licensor (but not in any way that suggests that they endorse you or your use of the work).
* Share Alike: If you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.

When attributing this work, please include me.


