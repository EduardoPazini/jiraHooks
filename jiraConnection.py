from jira import JIRA
from dotenv import load_dotenv
from pathlib import Path

import requests
import os

# Set here the path of your .env
env_path = Path('/home/eduardo')/'.env'
load_dotenv(dotenv_path=env_path)

workspace = os.getenv("WORKSPACE")
email = os.getenv("EMAIL")
token = os.getenv("TOKEN")

class Config():
    def __init__(self):
        self.jira = open_connection(workspace, email, token)

    def get_all_infos(self, initial, final):
        infos = ''
        for issue in self.jira.search_issues('project=CLIEN ORDER BY key ASC', startAt=0, maxResults=None):
            key = (int(issue.key.split('-',1)[1]))
            if(key >= initial and key <= final):
                if(issue.fields.description != None):
                    psw = get_password(issue.fields.description)
                    if (psw != -1):
                        infos = infos + structure_response(str(key), psw)
        archive(infos)

    def swap(self, args):
        if(args[0] > args[1]):
            temp = args[1]
            args[1] = args[0]
            args[0] = temp
        return args

# Function to open a connection with jira using workspace, email and token
def open_connection(workspace, email, token):
    jira = JIRA(server=workspace, 
        basic_auth=(email, token))
    return jira

def get_password(description):
    if(description.find('Senha:') != -1):
        aux = (description.split("Senha:", 1)[1])
        psw = (aux.split('\n', 1)[0].lstrip(' '))
    elif(description.find('senha:') != -1):
        aux = (description.split("senha:", 1)[1])
        psw = (aux.split('\n', 1)[0].lstrip(' '))
    else:
        return -1
    return psw

def structure_response(clien, psw):
    lineInfo = str('CLIEN-' + clien + ', ' + psw + '\n')
    return lineInfo

def archive(infos):
    file = 'infos.txt'
    try:
      with open(file, 'a') as f:
           f.write(infos)
    except OSError as e:
           print(f"Could not open file:", file)
           sys.exit()
    except IOError as e:
           print(f"Could not read/write file:", file)    
           sys.exit()