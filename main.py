import jiraConnection
import sys

jira = jiraConnection.Config()

# Get args regarding ClienInicial and ClienFinal from command line
args = sys.argv[1:]

if(int(args[0]) >= int(args[1])):
    print("Error: the final client is lowest than inicial client")
    sys.exit()

for clien in range(int(args[0]), int(args[1])):
    strClien = str(clien)
    psw = jira.get_description(strClien)
    
    if (psw != 'null'):
        jira.archive(strClien, psw)
        print ('CLIEN-' + strClien + ', ' + psw)