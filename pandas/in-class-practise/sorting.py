import pandas as pd

df_csv = pd.read_csv('../auto_mpg.csv')
df_csv

# sorting df by acceleration
df_csv.sort_values(by='acceleration', ascending=True, inplace=True)

df_csv.sort_values(by=['acceleration', 'horsepower'], ascending=[True,False])

# first the df will be sorted based on acceleration, then for same values of accleration
# it will be sorted based on horsepower values in descending order ( as we have
# set ascending=False)

## Apply function

df_csv.head()

# 1lbs = 0.453593 KGs
df_csv['weight_kg] = df_csv['weight'].apply(lambda x : x * 0.453593)
df_csv.head()

# for horsepower
# if it's < 90 -> low
# if it's >= 90 and < 150 -> medium
# if it's > = 150 -> high

df_csv['horsepower_category'] = df_csv['horsepower'].apply(lambda x: 'low' if x < 90 else 'medium if (x >= 90 and x < 150) else 'high')
df_csv.head()

