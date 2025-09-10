import pandas as pd

data = {'Category': ['A','B','A','B','A'],
        'Values': [10,20,30,40,50]}
data

df = pd.DataFrame(data)
pd


values_sum_by_category = df.gropuby('Category')['Values].sum()
# just the values_sum_by_category is pandas.core.generic.SeriesGroupBy object
# it only makes sense to apply sum aggregate function on gropuped data

# multiple aggregate function
# grouping by category and applying multiple agg func

res = df.groupby('Category')['Values'].agg(['sum', 'mean', 'count'])
res

# will print sum mean count


## Using a custom function
def range_func(x):
  return x.max() - x.min()

result = df.groupby('Category')['Values'].agg(range_func)
result

# if no agg func applied, the grouped obj remains a DataFrameGroupBy obj
# can use .apply() for more complex operations, but .agg() is preffered for aggregation tasks

df_csv = pd.read_csv('../auto_mpg.csv')
# avg acclrn by origin

df_csv.groupby('origin')['acceleration'].mean()

# avg accln by origin and model_year
df_csv.groupby(['origin', 'model_year'])['acceleration'].mean()


