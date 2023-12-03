# Code to generate a json file formatting for Davinci model

# import csv
# import json

# # Define the paths for your CSV input and JSON output files
# csv_file = '../dataset/StackOverflow_train_dataset.csv'
# json_file = '../output_davinci.json'

# # Initialize an empty list to store the JSON data
# json_data = []

# # Read the CSV file and convert it to JSON format
# with open(csv_file, 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for row in csv_reader:
#         # Assuming your CSV columns are 'prompt' and 'completion', change them as needed
#         prompt = row['comments']
#         completion = row['ratings']

#         # Create a dictionary with the desired format
#         entry = {
#             "prompt": prompt,
#             "completion": completion
#         }

#         # Append the entry to the JSON data list
#         json_data.append(entry)

# # Write the JSON data to the output file
# with open(json_file, 'w') as json_file:
#     json.dump(json_data, json_file, indent=2)

# print(f'CSV file "{csv_file}" has been converted to JSON format in "{json_file}".')



# # Code to generate file into GPT-3.5-Turbo model

import json

# def convert_to_new_format(old_data):
#     new_data = []
    
#     for entry in old_data:
#         new_entry = {
#             "messages": [
#                 {"role": "user", "content": entry["prompt"]},
#                 {"role": "assistant", "content": entry["completion"]}
#             ]
#         }
#         new_data.append(new_entry)
        
#     return new_data

# # Load the old data
# with open('../output_davinci.json', 'r') as file:
#     old_data = json.load(file)

# # Convert the old data to the new format
# converted_data = convert_to_new_format(old_data)

# # Save the converted data to a new file
# with open('../output_gptTurbo.json', 'w') as file:
#     json.dump(converted_data, file, indent=2)


# # Code to convert json to jsonl format
fine_tune_file = open('../output_gptTurbo.json')
fine_tune_data = json.load(fine_tune_file)

def json_to_jsonl(json_data, file_path):
    with open(file_path, "w") as file:
        for data in json_data:
            json_line = json.dumps(data)
            file.write(json_line + '\n')

json_to_jsonl(fine_tune_data, r"../output_gptTurbo.jsonl")



