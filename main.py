import jiraConnection

jira = jiraConnection.Config()

# Set here the numbers of projects CLIEN

clienInicial = X
clienFinal = Y


for clien in range(clienInicial, clienFinal):
    strClien = str(clien)
    psw = jira.get_description(strClien)
    
    if (psw != 'null'):
        jira.archive(strClien, psw)
        print ('CLIEN-' + strClien + ', ' + psw)