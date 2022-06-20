import pandas as pd
import csv

df = pd.read_csv('bright_stars.csv')
df.columns

del df["VMag"]
del df["Bayer Designation"]
del df["Spectral Class"]
del df["Luminosity"]

final_data = df.dropna()
final_data.reset_index(drop = True, inplace = True)

final_data.to_csv('delete.csv')
