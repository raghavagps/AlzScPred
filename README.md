
# AlzScPredict :- A Tool for Identification of Alzheimer's from Single Cell Genome using Deep Learning

A computational approach tool to predict Alzheimer's affected patients from their single cell RNA seq data.


## Introduction

Alzheimer's Disease is progressing as the most common cause of neurological disorder worldwide. 

This tool aims to use Artifical Neural Network (Deep Learning) model to classify Normal Control(NC) patients and Alzheimer’s Disease(AD) patients from
their single cell RNA seq data. The tool takes 10x single cell genomics data as input and predicts whether the patient is diseased or healthy with the help of highly trained model.

An excellent feature selection method called mRMR (Minimum Redundancy Maximum Relevance) was used to find out top 100 features for classification. 
Followed by Incremental Feature Selection (IFS) which led to identification of 35 conserved genes which act as promising biomarkers
in classification and prediction of Normal and Diseased patients.

Please read/cite the content about the AlzScPredict for complete information including algorithm behind the approach.
## Installation

Install my-project with pip

```bash
  pip install AlzScPredict
```
    
You if previously installed please update the python package to the latest version using the command below

```bash
  pip3 install --upgrade AlzScPredict
```
## Usage/Examples

After installation of the AlzScPredict package in your python enviornment. Import the library using the below code.


```python
import AlzScPredict
```
The AlzScPredict comes with 3 inbuilt modules . 

- Preprocessing Module.
- Model Load Module.
- Prediction Module.

Please import all 3 modules in your python enviornment using the code below.

```python
from AlzScPredict import preprocessing
from AlzScPredict import Model_Selection
from AlzScPredict import PredictionModule

```

After importing all the important pre requisites. You can follow the demo below for your case.


```python
import pandas as pd
df = pd.read_csv("Your file path here")

#Takes single cell data in form of dataframe with cells in rows and features in columns. Returns preprocessed dataframe.
processed = preprocessing.preprocess_data(df)

# Load the model with the code below. This takes no arguments.
my_model = Model_Selection.load_model()

# Prediction:- Execute the code below to get the output. It takes 2 arguments i.e 
# preloaded model and the processed dataframe with 35 features.

PredictionModule.predict_patient(my_model,processed)

```

## Used By

This project is used by the following companies:

- Company 1
- Company 2


## Authors

- Aman Srivastava.
- Akanksha Jarwal. 
- [Prof. G.P.S. Raghava](https://www.github.com/octokatherine)

## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

