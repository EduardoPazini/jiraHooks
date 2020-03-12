# JiraHooks

The purpose of the code is to get all passwords for each client registered with Jira, the information is exported to a txt document.

# How to use

1) Set your credentials in jiraConnection.py

```
# Set here the credentials

#Set here your workspace/server
workspace = 'workspace'

email = 'email'

#Set here your jira security token
token = 'token'
```

2) Install and set the virtual enviroment

```
python -m venv env
source env/bin/activate
```

3) Install the packages required
   
```
pip install -r requirements.txt
```

4) Just run the command and wait until it finishes, the time to run depends your clienInicial and clienFinal

```
$ python3 main.py <clienInicial> <clienFinal>
```
```
#Exemple to get passwords between CLIEN-42 and CLIEN-69:
$ python3 main.py 42 69
```