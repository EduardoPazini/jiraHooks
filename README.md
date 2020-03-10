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

2) Define the clien inicial and clien final in main.py

```
# Set here the numbers of projects CLIEN

clienInicial = X
clienFinal = Y
```

3) Install and set the virtual enviroment

```
python -m venv env
source env/bin/activate
```

4) Install the packages required
   
```
pip install -r requirements.txt
```

5) Just run the command and wait until it finishes. There is no loading screen, with all CLIEN and password, the time to run depends your clienInicial and clienFinal defined in main.py

```
python3 main.py
```