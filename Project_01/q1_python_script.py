import pandas as pd

df = pd.read_csv('drybean.csv')
answer_1 = df.head(5)
answer_2 = df.columns.tolist()
answer_3 = df.shape
answer_4 = df.nunique()

print("======================== Answer_1: ========================")
print(answer_1)
print("======================== Answer_2: ========================")
print(answer_2)
print("======================== Answer_3: ========================")
print(answer_3)
print("======================== Answer_4: ========================")
print(answer_4)