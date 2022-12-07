#!/usr/bin/env python
from __future__ import print_function
import sys
"""
# *********************** 72 spaces ***********************************
DESCRIPTION

Script to reformat bibtex reference library into bibitems for specific
scientific journals.


BACKGROUND

Tne ScholarOne Manuscript vendor used by Protein Science does not accept
bibtex library files. As per the instructions to authors, you are stuck
with using a bibilography environment and the bibitems. This is a tedious
and error prone to do by hand.

The tex stackexchange user Ixy published on-line a python2 script that I
repurposed for Protein Science and python3. It is not all inclusive. Many
edge cases remain unaddressed. You will still have to check all references
manually.

The are other solutions to this problem. You are supposed to be able to
generate at *.bbl file from your lib file by running latex, bibtex, latex,
and latex on your bib file. The bbl file contains the bibitems. I recommend
this approach whenever possible. It is superior to this solution. However,
I had no luck with this approach at 1 AM on the night of manuscript submission.

There is also matlab solution. I do not have access to matlab.

Source:
(https://tex.stackexchange.com/questions/124874/
converting-to-bibitem-in-latex)

Author of inspiring code: Ixy, a secretive tex stackexchange user.


USAGE

bib2item3.py refs.bib



 Copyright Notice
 ================

 Copyright (c) 2019 Board of Regents for the University of Oklahoma

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation file
 (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge,
 publish, distribute, sublicense, and/or sell copies of the Software,
 and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
 CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# *********************** 72 spaces ***********************************

  Blaine Mooers, PhD
  blaine@ouhsc.edu
  975 NE 10th St, BRC 466
  Department of Biochemistry and Molecular Biology
  College of Medicine
  Stephenson Cancer Center
  University of Oklahoma Health Sciences Center,
  Oklahoma City, OK, USA 73104

Copyright 2019
Univeristy of Oklahoma Board of Regents
MIT Licence

11/8/19


HISTORY

Initialized on November 8, 2019 by Blaine Mooers.


Improved data collection by adding UTF9 compatibility,
closing file after writing, allowing for supscripts and superscripts
in Latex format, and corperate author instances (names without commas).
Melodie Chen-Glasser
mglasser@mines.edu
Colorado School of Mines
2022/12/07

FUTURE

Make functions for other specific journals.
Fix exception handling.
Run flake8.
Run Pep8
"""


def protein_science(bibtex):
    psUsage = """
    Opens a bibtex library that contains only the citations for one
    manuscript. The abbreviation for the journal titles follow
    Chemical Abstracts Service Source Index, 1985.
    Note that page numbers must be inclusive.

    This function is configured for Protein Science. See
    https://onlinelibrary.wiley.com/page/journal/1469896x/homepage/\
      forauthors.html#references

    Journal article
    1. King VM, Armstrong DM, Apps R, Trott JR (1998) Numerical
    aspects of pontine, lateral reticular, and inferior olivary
    projections to two paravermal cortical zones of the cat
    cerebellum. J Comp Neurol 390:537-551.

    Book:
    2. Voet D, Voet JG (1990) Biochemistry, John Wiley & Sons, New York.

    Book Chapter:
    3. Gilmor ML, Rouse ST, Heilman CJ, Nash NR, Levey AI,
    Receptor fusion proteins and analysis. In: Ariano MA, Ed.
    (1998) Receptor localization. Wiley-Liss, New York, pp 75-90.

    Electronic Media:
    4. Bio-Xplor, Version 1.0. New York: Biostructure Inc.; 1991.

    Journal article with PMID included (optional):
    5. Wood CE, Appt SE, Clarkson TB, Franke AA, Lees CJ, Doerge DR,
    Cline JM. Effects of high-dose soy isoflavones and equol on
    reproductive tissues in female cynomolgus monkeys.
    PMID: 16723506 [Medline]
    """
    print(psUsage)
    with open(home + outfilestem + '.txt', 'w', encoding='UTF8') as oitems:

      print()
      r = bibtex.split('\n')
      i = 0
      while i < len(r):
          line = r[i].strip()
          if not line: i += 1
          if '@' == line[0]:
            code = line.split('{')[-1][:-1]
            # Note the venue == journal
            title = venue = volume = number = pages = year = publisher = authors = None
            output_authors = []
            i += 1
            while i < len(r) and '@' not in r[i]:
              line = r[i].strip()
              #print(line)
              if line.startswith("title"):
                title = line.split('{', 1)[-1][:-2]
              elif line.startswith("journal"):
                venue = line.split('{', 1)[-1][:-2]
              elif line.startswith("volume"):
                volume = line.split('{', 1)[-1][:-2]
              elif line.startswith("number"):
                number = line.split('{', 1)[-1][:-2]
              elif line.startswith("pages"):
                pages = line.split('{', 1)[-1][:-2]
              elif line.startswith("year"):
                year = line.split('{', 1)[-1][:-2]
              elif line.startswith("publisher"):
                publisher = line.split('{', 1)[-1][:-2]
              elif line.startswith("author"):
                authors = line[line.find("{")+1:line.rfind("}")]
                if authors.find(',') == -1:
                  output_authors.append(authors)
                else:
                  for LastFirst in authors.split(' and '):
                    lf = LastFirst.replace(' ', '').split(',')
                    assert len(lf) == 2, "Author name has more than one comma " + ",".join(lf)
                    last, first = lf[0], lf[1]
                    output_authors.append("{} {}".format(last, first))
              i += 1

            oitems.write("\\bibitem{%s}" % code)
            oitems.write("\n")
            if len(output_authors) == 1:
                oitems.write(output_authors[0] + " ({}) ".format(year),)
            else:
                oitems.write(", ".join(_ for _ in output_authors)
                  + " ({}) ".format(year))
            if title:
                oitems.write("{}.".format(title))
            if venue:
                venue2 = venue.replace('.','')
                oitems.write(" {}".format(" ".join([_.capitalize() for _ in venue2.split(' ')])),)
                if volume:
                    oitems.write(" {}:".format(volume))
                if pages:
                    pages2 = pages.replace('--','-')
                    oitems.write("{}.".format(pages2) if number else "{}.".format(pages2))
            if publisher and not venue:
                oitems.write(" {}.".format(publisher))
            oitems.write("\n")
            oitems.write("\n")
    return


# *********************** __main__ ************ 72 spaces *************
""" In this section, select the function specific to your target
journal.
"""
if __name__ == '__main__':
    # Set the name of the output file.
    outfilestem = 'proteinScienceBibItems'
    home = 'D:/projects/bib2item3/'
    # Set the name of the input file.
    try:
        f = open(sys.argv[1],"r")
    except:
        print('Please provide name of bib file!')
        print('Usage: bibtex2item.py manuscirpt.bib')
    bibtex = f.read()
    # print(bibtex)
    # Convert the bibtex into bibitems for Protein Science
    protein_science(bibtex)
    # iucr(bibtex)
    # pnas(bibtex)
    # jbc(bibtex)
    # nar(bibtex)
    # rna(bibtex)
