import pandas as pd
import openai 
import pause
import csv

df = pd.read_csv("SO_Workflow_Data.csv")
openai.api_key = '<Your_API>'

df = df.iloc[7048:]
print(df[['Body']].head(5))

def analyze_gpt35(text):
    messages = [
        # {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text. 
        #                                 If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following product review and determine if the sentiment is: positive or negative. Return answer in single word as either positive or negative: {text}"""}
        ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages,
        max_tokens=1,
        request_timeout = 40,
        n=1,
        stop=None,
        temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()

    return response_text

ratings = []

csv_file = 'Out.csv'
header = ['Body','Value']

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)


for index, row in df.iterrows():
    sent = analyze_gpt35(row['Body'])
    print(sent)
    ratings.append(sent)
    # pause.seconds(20)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([row['Body'],sent])

# df['predicted_gpt35'] = df['Body'].apply(analyze_gpt35)
df['predicted_gpt35'] = ratings

print(df.head(10))

# df.to_csv('SO_Stackoverflow_Data.csv', index=False)