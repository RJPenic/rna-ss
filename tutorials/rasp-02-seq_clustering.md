# RNA Structure Prediction (RASP) - 02 - Sequence Clustering
## Sequence Clustering
When we train and evaluate prediction models, it is important to prevent potential data leaks between training and evaluation datasets.
An example of a data leak is when the same (or similar) data sample appears in both training and test datasets.
When it comes to RNAs and its structures, we prevent such cases by utilizing sequence clustering where we cluster similar RNA sequences together.
Clustering information is then used during the data split, where we make sure that sequences from the same cluster do not end up in different data splits.

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

**TASK**: Implement a Python method that will find all CT files in the given directory, load their RNA sequences and then save them to the specified FASTA file (usage example: `save_to_fasta(input_dir="./cts_dir", output_fasta_file="./data.fasta")`). Use your method to save all RNA sequences from the _ArchiveII_ dataset into a single FASTA file.

## MMSeqs2
_MMSeqs2_ is one of the most popular sequence clustering tools and can be used to cluster both protein and RNA/DNA sequences.
It offers many parameters where we can tune the "definition" of sequence similarity, but for now we'll focus on the two main options: '_--min-seq-id_' and '_-c_'.

First of all, let's quickly explain how _MMSeqs2_ works. 

When you use _MMSeqs2_, your command will usually look something like this:
```
mmseqs easy-cluster --min-seq-id <MINIMUM SEQUENCE IDENTITY> -c <MINIMUM COVERAGE> --threads <NUMBER OF THREADS> <INPUT FASTA> <OUTPUT FILES PREFIX> <TEMPORARY DIRECTORY>
```

We used three options:
- `MINIMUM SEQUENCE IDENTITY`
  - The higher this value is, the stricter your similarity definition is.
  - If you put this value to 1.0, only sequences that can be perfectly aligned to each other will be considered similar (e.g. ACUG and ACUGUG) 
- `MINIMUM COVERAGE`
  - The lower this value is, the more lenient we are when it comes to sequence length differences.
  - If you put this value to 0.0, even pairs of sequences with extremely different lengths can be clustered together.
- `NUMBER OF THREADS`
  - Define number of threads that will be used during the clustering. More threads usually means faster clustering (but be aware of the number of CPUs you have on your server and of other people that are using the same server).

Alongside the options, we also defined three files/directories:
- `INPUT FASTA`
  - FASTA file with sequences we want to cluster.
- `OUTPUT FILES PREFIX`
  - Prefix of the files that _MMSeqs2_ will output.
- `TEMPORARY DIRECTORY`
  - Path to the directory where _MMSeqs2_ will save its temporary files during the clustering.

Once the clustering is done, _MMSeqs2_ will output three files:
- `<OUTPUT FILE PREFIX>_cluster.tsv`
  - Tab-separated file describing resulting clusters.
  - Consists of two columns where the first column represents cluster ID and the second one represents ID of the sequence in the cluster.
- `<OUTPUT FILE PREFIX>_rep_seq.fasta`
  - Ordinary FASTA file containing sequences from the input FASTA file that are also cluster representatives.
  - Number of sequences in this file is equal to the number of clusters.
  - This file is usually taken when we want a non-redundant version of the input dataset.
- `<OUTPUT FILE PREFIX>_all_seqs.fasta`
  - File that contains clustering information in a FASTA-like format.

Use `--help` option to learn about additional options:
```
mmseqs easy-cluster --help
```

**TASK**: Collect RNA sequences from the _ArchiveII_ dataset and cluster them with _MMSeqs2_ (use `--min_seq_id 0.9` and `-c 0.8`). Check the output files. How many clusters are there? What's the distribution of cluster sizes (number of sequences in the cluster)? What happened with duplicate sequences? Did they end up in the same clusters? Try clustering again but this time with different clustering arguments. Try increasing/decreasing `--min_seq_id` and/or `-c`. What happens and why?

## Additional information:
- https://en.wikipedia.org/wiki/FASTA_format
- https://mmseqs.com/latest/userguide.pdf
- https://sites.google.com/view/cd-hit
