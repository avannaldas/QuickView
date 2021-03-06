'''
Title: QuickView
Purpose: Provides a Glance at the dataset with one line of code!
GitHub: http://github.com/avannaldas/QuickView
Author: Abhijit Annaldas (Twitter @avannaldas)
'''

import pandas as _pd
import matplotlib.pyplot as _plt
from matplotlib.pyplot import cm

'''Number of rows in the dataframe'''
row_count = -1

'''Number of columns in the dataframe'''
column_count = -1

''' List of numeric column names'''
numeric_column_names = []

'''List of text column names'''
text_column_names = []

'''List of categorical column names'''
categorical_column_names = []

'''Dict of Column names and distinct categrical values'''
categorical_column_values = dict()

''' Dict of Column names and number of distinct categrical values'''
categorical_column_values_count = dict()

'''Pandas dataframe object containing rows with at least one null/na values'''
rows_with_nulls = _pd.DataFrame()

'''Dict of Column names and number of null/na values'''
columnwise_null_values_count = dict()

'''Pandas dataframe object with min, max, mean and std of all numeric columns'''
min_max_mean_std = _pd.DataFrame()

'''Indicates whether the visualization is complete, values for all the member variables are updated after visualize() method is complete'''
loaded = False
#

def visualize(df, print_summaries=True, cat_pthreshold=5, cat_cthreshold=-1):

    row_count = df.shape[0]

    column_count = df.shape[1]

    rows_with_nulls = df[_pd.isnull(df).any(axis=1)]

    numeric_types = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64', 'int', 'float', 'long', 'complex']
    numeric_column_names = list(df.select_dtypes(include=numeric_types).columns)

    __text_column_names = list(df.select_dtypes(exclude=numeric_types).columns)
    for c in __text_column_names:
        if (((df[c].nunique()/row_count) * 100)  < cat_pthreshold) or (df[c].nunique()  < cat_cthreshold):
            categorical_column_names.append(c)
            categorical_column_values[c] = df[c].unique()
            categorical_column_values_count[c] = df[c].nunique()
        else:
            text_column_names.append(c)

    for c in list(df.columns):
        if df[c].isnull().sum() > 0:
            columnwise_null_values_count[c] = df[c].isnull().sum()

    minSumm = df.min(axis=0, skipna=True, numeric_only=True)
    maxSumm = df.max(axis=0, skipna=True, numeric_only=True)
    meanSumm = df.mean(axis=0, skipna=True, numeric_only=True)
    stdSumm = df.std(axis=0, skipna=True, numeric_only=True)
    min_max_mean_std = _pd.DataFrame(dict(min=minSumm, max=maxSumm, mean=meanSumm, std=stdSumm), index=stdSumm.index)

    loaded = True

    if print_summaries == True:
        print()
        print('Here is a summary of the Dataset, aka Quick View :P ...')
        print()
        print('Rows count: ' + str(row_count))
        print('Columns count: ' + str(column_count))
        print()
        print('Number of rows having null value(s): ' + str(rows_with_nulls.shape[0]))
        print()
        print('Numeric Columns: ' + (', '.join(numeric_column_names)))
        print()
        print('Categorical Columns: ' + (', '.join(categorical_column_names)))
        print()
        print('Text Columns: ' + (', '.join(text_column_names)))
        print()
        print('Columns with null values...')
        for k, v in columnwise_null_values_count.items():
            print(k + ' : ' + str(v))

        print()
        print('Distinct values in categorical columns...')
        for col, vals in categorical_column_values.items():
            print('{Column Name}: ' + col + ' {Values}: ' + ((', ').join(str(v) for v in vals)))
            print()

        print('Min, Max, Mean and std...')
        print(min_max_mean_std)
        print()

    # START PLOTTING
    # Column-wise plot null count
    _plt.bar(range(len(columnwise_null_values_count)), columnwise_null_values_count.values(), align='center')
    _plt.xticks(range(len(columnwise_null_values_count)), columnwise_null_values_count.keys(), rotation='vertical')
    _plt.xlabel('Column names')
    _plt.ylabel('# of Null values')
    _plt.title('Column-wise null value counts')
    _plt.tight_layout()
    _plt.show()
    print()

    # Column-wise plot unique categorical values count
    _plt.bar(range(len(categorical_column_values_count)), categorical_column_values_count.values(), align='center')
    _plt.xticks(range(len(categorical_column_values_count)), categorical_column_values_count.keys(), rotation='vertical')
    _plt.xlabel('Categorical Column names')
    _plt.ylabel('# of Unique Categorical values')
    _plt.title('Categorical Columns and their unique categorical value counts')
    _plt.tight_layout()
    _plt.show()
    print()

    # Correlation Matrix...
    corr = df.corr()
    fig, ax = _plt.subplots(figsize=(8, 8))
    cb = ax.matshow(corr, interpolation='nearest', cmap=cm.Blues)
    fig.colorbar(cb)
    _plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
    _plt.yticks(range(len(corr.columns)), corr.columns)
    _plt.xlabel('Correlation Matrix')
    _plt.tight_layout()
    _plt.show()
    print()