# JiraHooks

The purpose of the code is to get all passwords for each client registered with Jira, the information is exported to a txt document.

# How to use

1) Create a file called .env, set your jira credentials in it, like this:

```
WORKSPACE=https://myServer.myDomain.net/

EMAIL=myEmail@myDomain.com

TOKEN=42isTheNumberOfLife
```

2) In jiraConnections.py, set the path of your .env:

```
# In my case, the path is 'home/eduardo'

env_path = Path('/home/eduardo')/'.env'
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

5) Just run the command and wait until it finishes, the time to run depends your clienInicial and clienFinal

```
$ python3 main.py <clienInicial> <clienFinal>
```
```
#Exemple to get passwords between CLIEN-42 and CLIEN-69:
$ python3 main.py 42 69
```