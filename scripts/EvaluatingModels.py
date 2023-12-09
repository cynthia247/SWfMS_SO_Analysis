import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np

# Load your predictions into a pandas DataFrame (replace 'your_predictions.csv' with your actual file path)
df = pd.read_csv('../dataset/StackOverflow_test_dataset.csv')
df1 = pd.read_csv('../result.csv')

# Extract the true sentiment labels and predicted sentiment labels
true_labels = df['ratings']
predicted_labels = df1['ratings']

print(true_labels)
print(predicted_labels)

# Calculate accuracy
accuracy = accuracy_score(true_labels, predicted_labels)
print(f'Accuracy: {accuracy:.2f}')

# Calculate precision
precision = precision_score(true_labels, predicted_labels, average='weighted')
print(f'Precision: {precision:.2f}')

# Calculate recall
recall = recall_score(true_labels, predicted_labels, average='weighted')
print(f'Recall: {recall:.2f}')

# f1score = f1_score(true_labels, predicted_labels, average='weighted')
f1score = (2 * precision * recall)/ (precision+recall)
print(f'F1 Score: {f1score:.2f}')
