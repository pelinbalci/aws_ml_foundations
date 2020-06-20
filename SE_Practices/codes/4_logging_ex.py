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
import logging


def read_csv():
    logging.info('Reading csv & Prind fixed acidity')
    df = pd.read_csv('/Users/pelin.balci/PycharmProjects/aws_ml_foundations/SE_Practices/inputs/winequality-red.csv', sep=';')
    print(df['fixed acidity'].head())
    return df


# ### Renaming Columns
def rename_cols(df):
    logging.info('Renaming the columns')
    df.columns = [label.replace(' ', '_') for label in df.columns]
    return df


# Create new values:
def create_new_values(df, column_name):
    median_value = df[column_name].median()
    df[column_name] = np.where(df[column_name] >= median_value, 'high', 'low')


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.getLogger().setLevel(logging.DEBUG)
    logging.info('Started')
    df = read_csv()
    df = rename_cols(df)
    logging.info('Creating new values')
    for label in df.columns[:-1]:
        create_new_values(df, label)
        print(df.groupby(label).quality.mean(), '\n')
    logging.info('Finished')


if __name__ == '__main__':
    main()


logging.debug('This message should appear on the console')