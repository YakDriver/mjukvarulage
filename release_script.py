import sys
import os

def main(*args):
    print("MJUKVARULAGE ----")
    for arg in args:
        try:
            print("kwarg: {}={}".format(*arg.split('=')))
        except (IndexError):
            print("  arg: {}".format(arg))

    print("All the environment variables:")
    print(os.environ,sep="\n")

    print("Version:", os.environ["VERSION"])
    print("Secure:", os.environ["SUPER_NEW_ENVIRONMENT_VARIABLE"])

    if os.environ["SUPER_NEW_ENVIRONMENT_VARIABLE"] == "super_secure_stuff":
        print("It worked!")
    else:
        print("It didn't work")
        
    return 0

if __name__ == "__main__":
    # execute only if run as a script
    sys.exit(main(*sys.argv[1:]))