# __QuickView__

### Installing QuickView
QuickView has been published to PyPI [here](https://pypi.python.org/pypi/QuickView/0.1). It can be installed with `pip install quickview` or by downloading the tar.gz file from PyPI or you can download this repository and install with `python setup.py install`

### Using QuickView
To use QuickView, you just need to import the package and call visualize method passing the pandas dataframe.  The method outputs useful summaries about the dataset, plots number of null values colum-wise and number of unique values in categorical columns. The project has just begun and there are many more types of plots coming up soon.

```python
import QuickView.DataFrameVisualizer as qv
import pandas as pd

# Just call the visualize method and pass the pandas dataframe
qv.visualize(pd.read_csv('data.csv'))
```

### QuickView.DataFrameVisualizer.visualize() Parameters
|Parameter Name | Required | Description|
|:--------------|:---------|:-----------|
|df | Yes | Pandas Dataframe object |
| print_summaries | No, Default: True | Indicates whether the summaries are to printed or not |
| cat_pthreshold | No, Default: 5 | Percentage of Unique values in a text column below which, a column is to be considered as categorical |
| cat_cthreshold | No, Default: -1 | Count of Unique values in a text column below which, a column is to be considered as categorical |

If both _cat_pthreshold_ and _cat_cthreshold_ are provided, a column is considered as categorical if the unique values meet one of the threshold criteria. To ignore one of those, set the value to -1. By default, if unique values less than 5% of the total number of records, the column is considered categorical.

### QuickView.DataFrameVisualizer Properties
These properties reflect values only after calling `QuickView.DataFrameVisualizer.visualize()` method.

|Parameter Name | Description|
|:--------------|:-----------|
|row_count | Number of rows in the dataframe |
|column_count | Number of columns in the dataframe |
|numeric_column_names | List of numeric column names |
|text_column_names | List of text column names |
|categorical_column_names | List of categorical column names |
|categorical_column_values | Dict of Column names and distinct categrical values |
|categorical_column_values_counts | Dict of Column names and number of distinct categrical values |
|rows_with_nulls | Pandas dataframe object containing rows with at least one null/na values |
|columnwise_null_values_count | Dict of Column names and number of null/na values |
|loaded | Boolean, Indicates whether all the values have been updated |


#### Dataset Attribution
Dataset used in the QuickView Example.ipynb notebook was provided by HackerEarth for the [Machine Learning Challenge](https://www.hackerearth.com/challenge/competitive/machine-learning-challenge-one/machine-learning/bank-fears-loanliness/) I participated earlier. You can download the dataset from the challenge page link or try out with your own dataset.
