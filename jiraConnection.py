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
        line_count = 0
        with open('test.csv') as csv_file:
            infos = csv.reader(csv_file, delimiter=',')
            for row in infos:
                issue = self.jira.issue(row[1])
                iuguCode = row[0]
                issue.update(fields={'customfield_10129': iuguCode})
                line_count += 1
                print(f'On {row[1]}')
            print(f'\nProcessed {line_count} lines.')


# Function to open a connection with jira using workspace, email and token
def open_connection(workspace, email, token):
    jira = JIRA(server=workspace, 
        basic_auth=(email, token))
    return jira
