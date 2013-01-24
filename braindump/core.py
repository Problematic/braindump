from __future__ import print_function

import sys
from subprocess import call, Popen


def quick_add_message(file, message):
    try:
        with open(file, mode='a') as f:
            print(message, file=f)
    except IOError:
        sys.exit('Unable to append message to braindump file \'{0}\''.format(file))


def launch_editor(editor, file, wait=True):
    if wait is True:
        call(editor + ' ' + file, shell=True)
    else:
        Popen([editor + ' ' + file], shell=True)
