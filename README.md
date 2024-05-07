# bib2item3

## DESCRIPTION

Script to reformat Bibtex reference library into bibitems for specific 
scientific journals. Supports only Protein Science at this time.


## BACKGROUND

The ScholarOne Manuscript vendor used by Protein Science does not accept
Bibtex library files. Per the authors' instructions, you are stuck
with using a bibliography environment and bibitems. The bibitems are tedious
and error-prone to assemble by hand.

The tex Stackexchange user Ixy published online a python2 script that I 
repurposed for Protein Science and python3. It is not all-inclusive. Many 
edge cases remain unaddressed. You will still have to check all references 
manually.

There are other solutions to this problem. You should be able to  generate a 
*.bbl file from your lib file by running LaTeX, BibTeX, latex, and latex on 
your bib file. The *.bbl file contains the bibitems. I recommend using
this approach whenever possible. It is superior to the solution provided by my script. However,
I had no luck with this approach at 1 AM on the night of manuscript submission.

There is also a Matlab solution. 
I did not have access to Matlab at the time that I found this solution. 
Perhaps this solution can be run with an octave.


## Source of original script: 

Author of inspiring [code](https://tex.stackexchange.com/questions/124874/converting-to-bibitem-in-latex)
: Ixy, a secretive [tex StackExchange ](https://tex.stackexchange.com/) user.


## USAGE

bib2item3.py refs.bib

## Notes:

- The bib file should have only the citations that you want to include in your manuscript.
- The names of the journals should have the proper abbreviations. 
- The citations in the bib file should be in alphabetical order because this script does not sort them.
- You should be able to copy the output into a bibliography environment in your LaTeX file. 


## To Be Done

- run flake8 and edit
- run pylint and edit
- develop test functions
- improve error handling


