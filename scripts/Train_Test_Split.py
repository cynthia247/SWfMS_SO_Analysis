from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv('../StackOverflow.csv')
X = df[['comments']]
Y = df[['ratings']]

train_df, test_df = train_test_split(df, test_size=0.3, random_state=42, shuffle=True)

print(train_df)
print(test_df)
train_df.to_csv('../dataset/StackOverflow_train_dataset.csv', index = False)
test_df.to_csv('../dataset/StackOverflow_test_dataset.csv', index=False)