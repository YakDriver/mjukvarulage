import sys

def main(*args):
    print("MJUKVARULAGE ----")
    for arg in args:
        try:
            print("kwarg: {}={}".format(*arg.split('=')))
        except (IndexError):
            print("  arg: {}".format(arg))

    return 0

if __name__ == "__main__":
    # execute only if run as a script
    sys.exit(main(*sys.argv[1:]))