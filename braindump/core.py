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
    shell_string = '{0} "{1}"'.format(editor, file)
    if wait is True:
        call(shell_string, shell=True)
    else:
        Popen([shell_string], shell=True)
