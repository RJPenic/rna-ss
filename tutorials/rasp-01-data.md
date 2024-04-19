# RASP - 01 - Data

## Data Download
To evaluate and train our structure prediction tools we need annotated secondary structures (the more the better).
In this tutorial we are going to use the popular [_bpRNA-1m_ dataset](https://bprna.cgrb.oregonstate.edu/index.html) which contains over 100,000 known secondary structures.
Download the _BPSeq_ files provided on the _bpRNA-1m_ website and unzip the downloaded files.

## BPSeq File Format (_.bpseq_)
Let's check what's inside of the _BPSeq_ files we just downloaded. Open one of the files in the preferred text editors.

_BPSeq_ format is one of the most popular ways to "encode" the secondary structure where every row describes the pairing status of a specific nucleotide in the RNA.
The structural information in the _BPSeq_ format is denoted in three columns:
- The first column contains the sequence position, starting at one.
- The second column contains the base in one-letter notation.
- The third column contains the pairing partner of the base if the base is paired. If the base is unpaired, the third column is zero.

Additionally, _BPSeq_ files often contain comments prefixed with the '_#_' symbol. These are usually present at the beginning of the file and can be ignored.

BPSeq file example:
```
# bpRNA File:bpRNA_CRW_1.bpseq
# Original Source:Gutell Lab CRW (http://www.rna.ccbb.utexas.edu/DAT/3C/SBPI/index.php); Original File:AB002635.bpseq; Accession ID:AB002635;
1 A 0
2 C 302
3 A 301
4 C 300
5 A 0
6 U 299
7 G 298
8 C 297
9 A 0
10 A 0
11 G 47
```

## Dot Bracket File Format (_.dbn_)
Another popular way to represent the secondary structure is dot bracket notation. Dot bracket files usually consists of three rows:
- The first line is a title and starts with a ">" character.
- The second line contains the sequence.
- The third line contains structure information in dot-bracket notation.
  - The dot/period "." represents an unpaired nucleotide.
  - An open-parenthesis "(" represents the 5'-nucleotide in a pair, and the matching closing parenthesis ")" represents the 3'-nucleotide in the pair.
  - Other "bracket"-type symbols can be used to represent basepairs, thereby allowing pseudo-knots to be encoded.
  - Example: `<(.>)` = First nucleotide is paired with the fourth one, second one is paired with the last one and third one is unpaired.
 
Implement a python script which will convert given '_.bpseq_' file into '_.dbn_' format (usage example: `python convert input.bpseq output.dbn`).

Dot Bracket file example:
```
>A pseudo-knot structure
GAUGGCACUCCCAUCAAUUGGAGC
(((((..<<<))))).....>>>.
```

## Secondary Structure Visualization

## Exploratory Data Analysis

## Sources
- https://bprna.cgrb.oregonstate.edu/
- https://www.ibi.vu.nl/programs/k2nwww/static/data_formats.html
- https://rna.urmc.rochester.edu/Text/File_Formats.html
