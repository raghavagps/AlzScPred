
# AlzScPred :- A Tool for Identification of Alzheimer's from Single Cell Genome using Deep Learning

A computational approach tool to predict Alzheimer's affected patients from their single cell RNA seq data.


## Introduction

Alzheimer's Disease is progressing as the most common cause of neurological disorder worldwide. 

This tool aims to use Artifical Neural Network (Deep Learning) model to classify Normal Control(NC) patients and Alzheimer’s Disease(AD) patients from
their single cell RNA seq data. The tool takes 10x single cell genomics data as input and predicts whether the patient is diseased or healthy with the help of highly trained model.

An excellent feature selection method called mRMR (Minimum Redundancy Maximum Relevance) was used to find out top 100 features for classification. 
Followed by Incremental Feature Selection (IFS) which led to identification of 35 conserved genes which act as promising biomarkers
in classification and prediction of Normal and Diseased patients.

Please read/cite the content about the AlzScPred for complete information including algorithm behind the approach.
## Reference
Srivastava et al. Prediction of Alzheimer’s Disease from Single Cell Transcriptomics Using Deep Learning. <a href="https://europepmc.org/article/PPR/PPR690064"><font color=blue>bioRxiv; 2023. DOI: 10.1101/2023.07.07.548171</font></a>.

## Installation

Install my-project with pip

```bash
  pip install AlzScPred
```
    
You if previously installed please update the python package to the latest version using the command below

```bash
  pip3 install --upgrade AlzScPred
```
## Usage/Examples

After installation of the AlzScPredict package in your python enviornment. Import the library using the below code.


```python
import AlzScPred
```
The AlzScPredict comes with 1 inbuilt module . 

- Prediction Module

Please import the modules in your python enviornment before executing the code below.

```python
from AlzScPred import Validation

```

After importing all the important pre requisites. You can follow the demo below for your case.


```python
import pandas as pd
df = pd.read_csv("Your file path here")

# Prediction:- Execute the code below to get the output. It takes 1 argument i.e the dataframe with features in columns and rows as cells.

Validation.predict_patient(df)

```

Note: Please make sure that your single cell data file is prepared in the above example.csv format. And the file should also contain the read count data for the selected 35 genes in the above 35_genes.txt file.

## Output

The output of the code can be viewed in your python output terminal. Example can be seen in the output.png file.
## Authors

- [Aman Srivastava](https://github.com/AmanSriv97).
- Akanksha Jarwal. 
- Anjali Dhall.
- Sumeet Patiyal.
- [Prof. G.P.S. Raghava](https://webs.iiitd.edu.in/raghava/)
