# -*- coding: utf-8 -*-
"""Copia de fcc_predict_health_costs_with_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ur1Ve9DKzFwcLJ1j8GUPrYCUt5DMbNmv

*Note: You are currently reading this using Google Colaboratory which is a cloud-hosted version of Jupyter Notebook. This is a document containing both text cells for documentation and runnable code cells. If you are unfamiliar with Jupyter Notebook, watch this 3-minute introduction before starting this challenge: https://www.youtube.com/watch?v=inN8seMm7UI*

---

In this challenge, you will predict healthcare costs using a regression algorithm.

You are given a dataset that contains information about different people including their healthcare costs. Use the data to predict healthcare costs based on new data.

The first two cells of this notebook import libraries and the data.

Make sure to convert categorical data to numbers. Use 80% of the data as the `train_dataset` and 20% of the data as the `test_dataset`.

`pop` off the "expenses" column from these datasets to create new datasets called `train_labels` and `test_labels`. Use these labels when training your model.

Create a model and train it with the `train_dataset`. Run the final cell in this notebook to check your model. The final cell will use the unseen `test_dataset` to check how well the model generalizes.

To pass the challenge, `model.evaluate` must return a Mean Absolute Error of under 3500. This means it predicts health care costs correctly within $3500.

The final cell will also predict expenses using the `test_dataset` and graph the results.
"""

# Commented out IPython magic to ensure Python compatibility.
# Import libraries. You may or may not use all of these.
!pip install -q git+https://github.com/tensorflow/docs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
  # %tensorflow_version only exists in Colab.
#   %tensorflow_version 2.x
except Exception:
  pass
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

#import tensorflow_docs as tfdocs
#import tensorflow_docs.plots
#import tensorflow_docs.modeling

# Import data
!wget https://cdn.freecodecamp.org/project-data/health-costs/insurance.csv
dataset = pd.read_csv('insurance.csv')
dataset.tail()

# categorical to numerical data
df = dataset.copy()
df['sex'] = pd.factorize(df['sex'])[0]        # 0: female 1: male
df['smoker'] = pd.factorize(df['smoker'])[0]  # 0: no     1: yes
df['region'] = pd.factorize(df['region'])[0]  # 0: sw     1: se     2: nw     3: ne

df.tail()

# 80% data to train and 20% to test
train_df = df.sample(frac=0.8)
test_df = df[~df.isin(train_df)].dropna()

print(len(df), len(test_df), len(train_df))

# extracting labels
train_label = train_df.pop('expenses')
test_label = test_df.pop('expenses')

# creating the model
normalize = layers.experimental.preprocessing.Normalization()
normalize.adapt(data=train_df)

model = keras.Sequential([
    normalize,
    layers.Dense(32, activation='relu'),
    layers.Dense(16),
    layers.Dense(1)
])

model.summary()

# Compiling the model
model.compile(
    optimizer='adam',
    loss = 'mae',
    metrics = ['mae', 'mse']
)

model.build()

# Training the model
model.fit(
    train_df,
    train_label,
    epochs=100,
    validation_split=0.2,
    verbose=2
)

test_dataset = test_df
test_labels = test_label

# RUN THIS CELL TO TEST YOUR MODEL. DO NOT MODIFY CONTENTS.
# Test model by checking how well the model generalizes using the test set.
loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=2)

print("Testing set Mean Abs Error: {:5.2f} expenses".format(mae))

if mae < 3500:
  print("You passed the challenge. Great job!")
else:
  print("The Mean Abs Error must be less than 3500. Keep trying.")

# Plot predictions.
test_predictions = model.predict(test_dataset).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True values (expenses)')
plt.ylabel('Predictions (expenses)')
lims = [0, 50000]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims,lims)