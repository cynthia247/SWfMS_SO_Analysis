import pandas as pd
import openai 
import csv

df = pd.read_csv("SO_Workflow_Data.csv")
openai.api_key = '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'

df = df.iloc[7048:]
# df = df.head(100)
# print(df[['Body']].head(5))

def analyze_gpt35(text):
    messages = [
        {"role": "user", "content": f"""Analyze the following sentence and determine if the sentiment is: positive or negative. Return answer in single word as either positive or negative: {text}"""}
        ]

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:software-research-lab::8GuyXxwV",
        messages = messages,
        max_tokens=2,
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
# df['predicted_gpt35'] = ratings


# df.to_csv('SO_Stackoverflow_Data.csv', index=False)