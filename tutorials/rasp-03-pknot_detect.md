# RNA Structure Prediction (RASP) - 03 - Pseudoknot Detection

Before we try predicting the structure itself, let's try doing something a bit simpler. We'll try to predict whether or not a certain RNA folds into a structure with pseudoknot based on the RNA sequence alone. Basically, we are doing a relatively simple binary classification where the input in our model is RNA sequence.

<p align="center">
 <img src="../imgs/pknot_detect.png" width="500">
</p>

## Training and evaluation data
Before we start dealing with anything else, we need to split our dataset into training, validation and test sets. Use _ArchiveII_ dataset as the starting point, remove sequence duplicates, cluster its sequences with _MMSeqs2_ and split the dataset into three parts accordingly (Reminder: RNAs from the same cluster should be in the same data split).

You will also have to assign a label to each RNA (1 if its structure contains pseudoknot and 0 if it doesn't). Save the sequences with their labels into a CSV file (make a separate CSV file for each dataset).

## Sequence featurization

## Model and training

## Results
