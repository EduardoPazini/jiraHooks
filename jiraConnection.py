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

    def get_description(self, clien):
        response = requests.get(workspace + '/rest/api/2/issue/CLIEN-' + str(clien),
            auth=(email, token))

        res = ''
        for x in range(2, 15):
            res = res + response.text[x]
        
        if(res == 'errorMessages'):
            return 'null'
        else:
            issue = self.jira.issue(str('CLIEN-' + clien))
            description = (issue.fields.description)

            if(description == None):
                psw = 'null'
            elif(description.find('Senha:') != -1):
                aux = (description.split("Senha:", 1)[1])
                psw = (aux.split('\n', 1)[0].lstrip(' '))
            elif(description.find('senha:') != -1):
                aux = (description.split("senha:", 1)[1])
                psw = (aux.split('\n', 1)[0].lstrip(' '))
            else:
                psw = 'null';
            return psw           

    def archive(self, clien, psw):
        client = str('CLIEN-' + clien + ', ')
        info = str(client + psw + '\n')
        
        f = open('infos.txt', 'a')
        f.write(info)
        f.close()


# Function to open a connection with jira using workspace, email and token
def open_connection(workspace, email, token):
    jira = JIRA(server=workspace, 
        basic_auth=(email, token))
    return jira