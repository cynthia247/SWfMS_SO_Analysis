import pandas as pd
import re

df = pd.read_csv('SO_Workflow_Data.csv')

for index, row in df.iterrows():
    clean = re.compile('<.*?>')
    row['Body'] = re.sub(clean, '', row["Body"])
    

df.Body.replace(r'\s+', ' ', regex=True)
print(df[['Body']])
df.to_csv('SO_Workflow_Data.csv', index=False)


