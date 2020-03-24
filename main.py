import jiraConnection
import argsValidate
import sys

jira = jiraConnection.Config()

argsValidate.main(sys.argv)

if __name__ == "__main__":
    args = jira.swap(sys.argv[1:])
    jira.get_all_infos(int(args[0]), int(args[1]))