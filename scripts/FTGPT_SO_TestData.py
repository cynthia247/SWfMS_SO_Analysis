import pandas as pd
import openai 
import pause
import csv

df = pd.read_csv("../dataset/StackOverflow_test_dataset.csv")
openai.api_key = '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'

# df = df.iloc[382:]
print(df[['comments']].head(5))

def analyze_gpt35(text):
    messages = [
        # {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text. 
        #                                 If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following product review and determine if the sentiment is: positive or negative. Return answer in single word as either positive or negative: {text}"""}
        ]

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-1106:software-research-lab::8ICPoM94",
        messages = messages,
        max_tokens=2,
        request_timeout = 40,
        n=1,
        stop=None,
        temperature=0)
    
    response_text = response.choices[0].message.content.strip().lower()

    return response_text

ratings = []

csv_file = '../Out.csv'
header = ['comments','ratings']

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)


for index, row in df.iterrows():
    sent = analyze_gpt35(row['comments'])
    print(sent)
    ratings.append(sent)
    # pause.seconds(20)

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([row['comments'],sent])

# df['predicted_gpt35'] = df['Body'].apply(analyze_gpt35)
# df['predicted_gpt35'] = ratings

# print(df.head(10))

# df.to_csv('SO_Stackoverflow_Data.csv', index=False)