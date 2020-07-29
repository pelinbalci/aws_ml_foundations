#!/usr/bin/env python
# coding: utf-8

# # Refactor: Wine Quality Analysis
# In this exercise, you'll refactor code that analyzes a wine quality dataset taken from the UCI Machine Learning
# Repository [here](https://archive.ics.uci.edu/ml/datasets/wine+quality).
# Each row contains data on a wine sample, including several physicochemical properties gathered from tests,
# as well as a quality rating evaluated by wine experts.
# 
# The code in this notebook first renames the columns of the dataset and then calculates some statistics on how some
# features may be related to quality ratings. Can you refactor this code to make it more clean and modular?

import pandas as pd
import numpy as np
df = pd.read_csv('/Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/inputs/winequality-red.csv', sep=';')
df.head()


# ### Renaming Columns

# First Way:
new_df = df.copy()
new_df = new_df.rename(columns={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })

# Second Way:

second_df = df.copy()
labels = list(second_df.columns)
labels[0] = labels[0].replace(' ', '_')
labels[1] = labels[1].replace(' ', '_')
labels[2] = labels[2].replace(' ', '_')
labels[3] = labels[3].replace(' ', '_')
labels[5] = labels[5].replace(' ', '_')
labels[6] = labels[6].replace(' ', '_')
second_df.columns = labels

# Third Way
third_df = df.copy()
labels = list(third_df.columns)
for i in range(len(labels)):
    labels[i] = labels[i].replace(' ', '_')
third_df.columns = labels

# Best Way

df.columns = [label.replace(' ', '_') for label in df.columns]


# ### Analyzing Features

# Now that your columns are ready, you want to see how different features of this dataset relate to the quality rating
# of the wine. A very simple way you could do this is by observing the mean quality rating for the top and bottom half
# of each feature. The code below does this for four features. It looks pretty repetitive right now.
# Can you make this more concise?


# First Way:

def long_way(df):
    median_alcohol = df.alcohol.median()
    for i, alcohol in enumerate(df.alcohol):
        if alcohol >= median_alcohol:
            df.loc[i, 'alcohol'] = 'high'
        else:
            df.loc[i, 'alcohol'] = 'low'
    df.groupby('alcohol').quality.mean()

    median_pH = df.pH.median()
    for i, pH in enumerate(df.pH):
        if pH >= median_pH:
            df.loc[i, 'pH'] = 'high'
        else:
            df.loc[i, 'pH'] = 'low'
    df.groupby('pH').quality.mean()

    median_sugar = df.residual_sugar.median()
    for i, sugar in enumerate(df.residual_sugar):
        if sugar >= median_sugar:
            df.loc[i, 'residual_sugar'] = 'high'
        else:
            df.loc[i, 'residual_sugar'] = 'low'
    df.groupby('residual_sugar').quality.mean()

    median_citric_acid = df.citric_acid.median()
    for i, citric_acid in enumerate(df.citric_acid):
        if citric_acid >= median_citric_acid:
            df.loc[i, 'citric_acid'] = 'high'
        else:
            df.loc[i, 'citric_acid'] = 'low'
    df.groupby('citric_acid').quality.mean()

    return df

# Second Way:

def separately(df):
    import numpy as np
    median_alcohol = df.alcohol.median()
    median_pH = df.pH.median()
    median_sugar = df.residual_sugar.median()
    median_citric_acid = df.citric_acid.median()

    df['alcohol'] = np.where(df['alcohol'] >= median_alcohol, 'high', 'low')
    df.groupby('alcohol').quality.mean()

    df['citric_acid'] = np.where(df['citric_acid'] >= median_citric_acid, 'high', 'low')
    df.groupby('citric_acid').quality.mean()

    df['residual_sugar'] = np.where(df['residual_sugar'] >= median_sugar, 'high', 'low')
    df.groupby('residual_sugar').quality.mean()

    df['pH'] = np.where(df['pH'] >= median_pH, 'high', 'low')
    df.groupby('pH').quality.mean()

    return df


# Third Way:

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 

loc_df = df.copy()
for feature in loc_df.columns[:-1]:
    numeric_to_buckets(loc_df, feature)
    print('WITH LOC:')
    print(loc_df.groupby(feature).quality.mean(), '\n')


# Fourth Way:

def create_new_values(df, column_name):
    median_value = df[column_name].median()
    df[column_name] = np.where(df[column_name] >= median_value, 'high', 'low')


np_df = df.copy()
for label in np_df.columns[:-1]:
    create_new_values(np_df, label)
    print('WITH NP WHERE:')
    print(np_df.groupby(label).quality.mean(), '\n')


# Best Way -2
def create_values(df, column_name):
    median_value = df[column_name].median()
    df[column_name] = ['high' if x >= median_value else 'low' for x in df[column_name]]

best_df = df.copy()
for label in best_df.columns[:-1]:
    create_values(best_df, label)
    print('WITH FOR LOOP:')
    print(best_df.groupby(label).quality.mean(), '\n')

# NOTES:

# 1- Not working since after the first raw, it can't check the string values.
# df['alcohol'][df['alcohol'] >= median_alcohol] = 'my_high'
# df['alcohol'][df['alcohol'] < median_alcohol] = 'my_low'


# 2- Not working for string variables. It works only for numbers:
# df['alcohol'].values[df['alcohol'].values > median_alcohol] = 1
# df['alcohol'].values[df['alcohol'].values < median_alcohol] = -1


# 3- FALSE df[df[col] == "A"][col] = 1
#    TRUE df[col][df[col] == "A"] = 1


# 4- Write 11 if the value is bigger than 9, else they should be remain the same:
# df1['A'] = df1['A'].apply(lambda x: [y if y <= 9 else 11 for y in x])


# 5- Write True / False based on a condition
# df['equal_or_lower_than_4?'] = df['set_of_numbers'].apply(lambda x: 'True' if x <= 4 else 'False')

# When I applied 5th version in this data, I get [high] instead of high.
# df['newalcohol'] = df['alcohol'].apply(lambda x: ['low' if x < median_alcohol else 'high']) #gives high in a list

# Useful Links:
# https://datatofish.com/if-condition-in-pandas-dataframe/
# https://stackoverflow.com/questions/49857470/replace-value-in-pandas-dataframe-based-on-condition


