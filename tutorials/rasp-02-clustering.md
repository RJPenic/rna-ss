# RNA Structure Prediction (RASP) - 02 - Sequence Clustering
## Sequence Clustering
When we train and evaluate prediction models, it is important to prevent potential data leaks between training and evaluation datasets.
An example of a data leak is when the same (or similar) data sample appears in both training and test datasets.
When it comes to RNAs and its structures, we prevent such cases by utilizing sequence clustering where we cluster similar RNA sequences together.
Clustering information is then used during the data split, where we make sure that sequences from the same cluster don't end up in different datasets.

## FASTA File Format
FASTA format is a text-based format representing biological sequences.
A sequence begins with a greater-than character (">") followed by a description of the sequence (all in a single line). The next lines immediately following the description line are the sequence representation, with one letter per amino acid or nucleic acid, and are typically no more than 80 characters in length.

```
>sequence1
CACUUCCAAGGGGCCACACCCCCAG
GCCUCUUGACCCCCCG
>sequence2
AAGGAUUUUUUGGCAUUCC
>sequence3
GGGGCCUCACCCCCGUUUGUGGG
...
```

**TASK**: Implement a Python method that will find all BPSeq files in the given directory, load their RNA sequences and then save them to the specified FASTA file (usage: `save_to_fasta(input_dir=bpseqs_dir, fasta_file="output.fasta")`). Use your method to save all RNA sequences from the _bpRNA-1m_ dataset into a single FASTA file.

## MMSeqs2
MMSeqs2 is one of the most popular sequence clustering tools and can be used to cluster both protein and RNA/DNA sequences. It offers various parameters where we can tune our definition of sequence similarity.

**TASK**: Collect RNA sequences from the _bpRNA-1m_ dataset and cluster them with _MMSeqs2_.
