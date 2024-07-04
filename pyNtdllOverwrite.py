import argparse
from overwrite import overwrite_disk, overwrite_knowndlls, overwrite_debugproc


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--option', required=True, action='store', help='Option for library overwrite: \"disk\", \"knowndlls\" or \"debugproc\"')
    parser.add_argument('-p', '--path', required=False, default="", action='store', help='Path to ntdll file in disk (for \"disk\" option) or program to open in debug mode (\"debugproc\" option)')
    my_args = parser.parse_args()
    return my_args


def main():
    # Ntdll overwrite
    args = get_args()
    option = args.option
    if option == "disk":
        path = "C:\\Windows\\System32\\ntdll.dll"
        if args.path != "":
            path = args.path
        overwrite_disk(path)
    elif option == "knowndlls":
        overwrite_knowndlls()
    elif option == "debugproc":
        path = "c:\\windows\\system32\\calc.exe"
        if args.path != "":
            path = args.path
        overwrite_debugproc(path)
    else:
        pass


if __name__ == "__main__":
    main()