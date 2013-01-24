"""
braindump - record what's on your mind

Usage:
    braindump [options] [TOPIC]

Arguments:
    TOPIC                           Subject to braindump on, determines filename [default: braindump]

Options:
    -v --version                    Show version information
    -h --help                       Show this help screen
    -s --settings SETTINGS_FILE     Settings file to load
    -m MESSAGE                      Add a message without opening your editor
"""

from __future__ import print_function

import json
import os
import sys

from docopt import docopt

from braindump import __version__, core


def load_settings(settings_file=None):
    default_settings = {
        'braindump_dir': '~/braindump',
        'default_topic': 'braindump',
        'editor': os.environ.get('EDITOR', 'vi'),
        'file_ext': '.txt',
    }

    settings_file = settings_file if settings_file is not None else os.path.expanduser('~/.braindump')
    try:
        with open(settings_file) as f:
            loaded_settings = json.load(f)
    except IOError:
        sys.exit('braindump: Unable to load settings file \'{0}\''.format(settings_file))

    settings = dict(default_settings.items() + loaded_settings.items())
    settings['braindump_dir'] = os.path.expanduser(settings['braindump_dir'])

    return settings


def main():
    arguments = docopt(__doc__, version=__version__)
    settings = load_settings(arguments['--settings'])

    topic = arguments['TOPIC'] if arguments['TOPIC'] is not None else settings['default_topic']
    dumpfile = topic + settings['file_ext']
    dumpfile = os.path.join(settings['braindump_dir'], dumpfile)

    if arguments['-m'] is not None:
        core.quick_add_message(dumpfile, arguments['-m'])
    else:
        core.launch_editor(settings['editor'], dumpfile)
