# bib2item3

## DESCRIPTION

Script to reformat bibtex reference library into bibitems for specific 
scientific journals. 


## BACKGROUND

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


## Source of original script: 
(https://tex.stackexchange.com/questions/124874/
converting-to-bibitem-in-latex)

Author of inspiring code: Ixy, a secretive tex stackexchange user.


## USAGE

bib2item3.py refs.bib

#### Notes:

- The bib file should have only the citations that you want to include in your manuscript.
- The names of the journals should have the proper abbreviations. 
- The citatoins in the bib file should be in alphabetical order because this script does not sort them.
- You should be able to copy the output into a bibliography environment in your LaTeX file. 


## To Be Done

- run flake8 and edit
- run pylint and edit
- develop test functions
- improve error handling
