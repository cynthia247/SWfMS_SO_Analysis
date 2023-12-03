import os
import openai
openai.api_key = "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"

### Upload the file

# upload_response = openai.File.create(
#   file=open("../output_gptTurbo.jsonl", "rb"),
#   purpose='fine-tune'
# )

# file_id = upload_response.id
# print(upload_response)


### Create the model (ALERT: MAKE SURE TO RUN THIS COMMAND ONCE)
# File_id = "file-x0Tr0PdDbuHpxcBVnFkNSksc"

# # # # # fine_tune = openai.FineTuningJob.create(training_file="file-OU2AtlfnYF1KX6qzTT29sFIU", model="gpt-3.5-turbo")
# print(fine_tune)

# "organization_id": "org-83C60mEybrendvh4joSlMPGO"
# "id": "ftjob-ZYUR3JiNO4tt6YN8m3zgFAy0"

### Check the model's progress
# print(openai.FineTuningJob.retrieve("ftjob-MXQuXjSKtilpta4yzAAAyV38"))


### List 10 fine-tuning jobs
# print(openai.FineTuningJob.list(limit=10))


### Test the model

def analyze_gpt35(text):
    messages = [
        # {"role": "system", "content": """You are trained to analyze and detect the sentiment of given text. 
        #                                 If you're unsure of an answer, you can say "not sure" and recommend users to review manually."""},
        {"role": "user", "content": f"""Analyze the following product review and determine if the sentiment is: positive or negative. Return answer in single word as either positive or negative: {text}"""}
        ]

    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0613:software-research-lab::8GuyXxwV",
        messages = messages,
        max_tokens=1,
        request_timeout = 40,
        n=1,
        stop=None,
        temperature=0)
    
    response_text = response.choices[0].message.content

    return response_text


# sent = analyze_gpt35("""I have been using Rapidminer and created a series of processes which preform a standard set of tasks. Now, I want allow the user to dynamically set the parameters of a process at the start. 

# For example, when writing  a CSV, I want to prompt the user to type a string containing the location where it should be saved via some prompt (either at the start of the script, or at some other stage during the process.

# Is this possible via Rapidminer, or should I be creating some script to generate and runt he process on the fly?""")

# print(sent)