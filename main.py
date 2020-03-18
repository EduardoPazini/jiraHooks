import jiraConnection
import argsValidate
import sys

jira = jiraConnection.Config()

argsValidate.main(sys.argv)

if __name__ == "__main__":
    args = jira.swap(sys.argv[1:])

    for clien in range(int(args[0]), int(args[1])+1):
	    psw = jira.get_description(str(clien))

	    if (psw != 'null'):
	        jira.archive(str(clien), psw)
	        print ('CLIEN-' + str(clien) + ', ' + psw)