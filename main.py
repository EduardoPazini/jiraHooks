import jiraConnection
import argsValidate
import sys

jira = jiraConnection.Config()

argsValidate.main(sys.argv[1:])

if __name__ == "__main__":
    for clien in range(int(sys.argv[1]), int(sys.argv[2])+1):
	    psw = jira.get_description(str(clien))

	    if (psw != 'null'):
	        jira.archive(str(clien), psw)
	        print ('CLIEN-' + str(clien) + ', ' + psw)