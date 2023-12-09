import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def FindingPostsWithNegativeSentiments():
    df = pd.read_csv('../dataset/SO_Workflow_Data.csv')
    my_value = -1
    data = df.loc[df["RatingsGPTFineTuned"] == my_value]

    df = data[data['Body'].str.contains('genepattern', case=False)] 
    print(len(df))
    # df.to_csv('../dataset/fireworks_posts.csv', index=False)


def ReplacingUndefinedValues():
    df = pd.read_csv('../dataset/SO_Workflow_Data.csv')
    allowed_values = [1,0,-1]

    # Replace values not in the allowed list with 2
    df.loc[~df['ratings'].isin(allowed_values), 'ratings'] = 0

def ReplacingStringSentiments():
    df = pd.read_csv('../dataset/SO_Workflow_Data.csv')
    df['ratings'] = df['ratings'].replace('positive', 1)
    df['ratings'] = df['ratings'].replace('negative', -1)
    df['ratings'] = df['ratings'].replace('neutral', 0)
    print(df)


def MergeDF():
    # Merge df according to post id for getting the dates
    df1 = pd.read_csv('../dataset/WithAnswerDate.csv')
    df2 = pd.read_csv('../dataset/AssignedTopicGalaxy.csv')

    merged_df = pd.merge(df2, df1, on='Id', how='left')
    columns_to_include = ['Id', 'Title_x', 'Body_x', 'CreationDate', 'AcceptedAnswerDate', 'topic']

    # Create a new DataFrame with the selected columns
    df_new = merged_df[columns_to_include].copy()

    return df_new


def CalculateTimeComplexity(df):

    df = df[df['topic'] == 2]
    df = df.fillna('0001-01-01 00:00:00')
    df['time_interval'] = pd.Series(dtype=float)
    print(df['AcceptedAnswerDate'])
    df['CreationDate'] = pd.to_datetime(df['CreationDate'])
    df['AcceptedAnswerDate'] = pd.to_datetime(df['AcceptedAnswerDate'], errors = 'coerce')
    df['time_interval'] = df['AcceptedAnswerDate'] - df['CreationDate'] 

    df['complexity'] = df['time_interval'].dt.total_seconds() / 3600


    # Assuming df is your DataFrame with time interval data
    plt.scatter(df.index, df['time_interval'], c=df['time_interval'], cmap='viridis', alpha=0.7)
    plt.colorbar(label='Time Interval (in hours)')
    plt.xlabel('Question Index')
    plt.ylabel('Time Interval')
    plt.title('Scatter Plot of Time Intervals between Question and Accepted Answer')
    plt.show()

df = MergeDF()
# CalculateTimeComplexity(df)
FindingPostsWithNegativeSentiments()