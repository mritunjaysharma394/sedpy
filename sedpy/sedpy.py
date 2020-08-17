from __future__ import print_function  #Only for use in Python 2.6.0a2 and later
import re


def replace(oldstring, newstring, infile, dryrun=False):
    '''
    Sed-like Replace
    Usage: sedpy <Old string>  <Replacement String> <Text File>
    Example: sedpy 'xyz' 'XYZ' '/path/to/file.txt'
    '''
    linelist = []
    with open(infile) as f:
        for item in f:
            newitem = re.sub(oldstring, newstring,
                             item)  #String replacement taking place.
            linelist.append(newitem)
    if dryrun == False:
        with open(infile, "w") as f:
            f.truncate()
            for line in linelist:
                f.writelines(
                    line
                )  #Dry Run False means it will not be displayed in STDOUT, File will change internally.
    elif dryrun == True:
        for line in linelist:
            print(line, end='')  #Dry Run Shows the changes on STDOUT.
    else:
        exit(
            "Unknown option specified to 'dryrun' argument, Usage: dryrun=<True|False>."
        )