import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

df = pd.read_csv('housing.csv')
missing_column = df.columns[df.isnull().any()][0]
median_value = df[missing_column].median()

imputer = KNNImputer(n_neighbors=10)
df_imputed = pd.DataFrame(imputer.fit_transform(df.select_dtypes(include=[np.number])), columns=df.select_dtypes(include=[np.number]).columns)

imputed_value = df_imputed.loc[291, missing_column]
print([missing_column, median_value, imputed_value])