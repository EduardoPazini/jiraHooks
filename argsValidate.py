import sys
import os

def main(args):
    if len(sys.argv) == 3:
        try:
            args = int(sys.argv[1])
        except:
            print(f"Error: wrong argument {sys.argv[1]}, it should be an integer")
            sys.exit()

        try:
            args = int(sys.argv[2])
        except:
            print(f"Error: wrong argument {sys.argv[2]}, it should be an integer")
            sys.exit()
    
    else:
        print("Error: wrong number of arguments, it should have two")
        sys.exit()

if __name__ == '__main__':
    main(sys.argv)