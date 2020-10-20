from jira import JIRA
from dotenv import load_dotenv
from pathlib import Path

import csv
import requests
import os

# Set here the path of your .env
env_path = Path('/home/ruivo')/'.env'
load_dotenv(dotenv_path=env_path)

workspace = os.getenv("WORKSPACE")
email = os.getenv("EMAIL")
token = os.getenv("TOKEN")

class Config():
    def __init__(self):
        self.jira = open_connection(workspace, email, token)

    def post_infos(self):
        read_csv()
        '''
        for issue in self.jira.search_issues('project=CLIEN ORDER BY key ASC', startAt=0, maxResults=None):
            key = (int(issue.key.split('-',1)[1]))
            if(key >= initial and key <= final):
                created = issue.fields.created
                seg = issue.fields.customfield_10029
                infos = infos + structure_response(str(key), str(created), str(seg))
        archive(infos)
        '''


# Function to open a connection with jira using workspace, email and token
def open_connection(workspace, email, token):
    jira = JIRA(server=workspace, 
        basic_auth=(email, token))
    return jira


# Function to read a csv and atribute a variable
def read_csv():
    with open('test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        infos = ''
        for row in csv_reader:
            infos += row[0] + ',' + row[1] + '\n'
            line_count += 1
        print(f'Processed {line_count} lines.')
        return infos
