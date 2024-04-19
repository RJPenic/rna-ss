# RASP - 01 - Data

## Data Download
To evaluate and train our structure prediction tools we need annotated secondary structures (the more the better).
In this tutorial we are going to use the popular [_bpRNA-1m_ dataset](https://bprna.cgrb.oregonstate.edu/index.html) which contains over 100,000 known secondary structures.
Download the _BPSeq_ files provided on the _bpRNA-1m_ website and unzip the downloaded files.

## BPSeq File Format
Let's check what's inside of the _BPSeq_ files we just downloaded. Open one of the files in the preferred text editors.

_BPSeq_ format is one of the most popular ways to "encode" the secondary structure where every row represents pairing status of a specific nucleotide in the RNA.
The structural information in the _BPSeq_ format is denoted in three columns:
- The first column contains the sequence position, starting at one.
- The second column contains the base in one-letter notation.
- The third column contains the pairing partner of the base if the base is paired. If the base is unpaired, the third column is zero.

Additionally, _BPSeq_ files often contain comments prefixed with the '_#_' symbol. These are usually present at the beginning of the file and can be ignored.
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
## Secondary Structure Visualization

## Exploratory Data Analysis
