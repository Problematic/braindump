"""
braindump - record what's on your mind

Usage:
    braindump ls
    braindump [options] [TOPIC]

Arguments:
    ls                              Output a list of topic files
    TOPIC                           Subject to braindump on, determines filename [default: braindump]

Options:
    -v --version                    Show version information
    -h --help                       Show this help screen
    -s --settings SETTINGS_FILE     Settings file to load
    -m MESSAGE                      Add a message without opening your editor
"""

import json
import os
import sys

from docopt import docopt

from braindump import __version__
from braindump.core import FSDumper


def load_settings(settings_file=None):
    default_settings = {
        'braindump_dir': '~/braindump',
        'default_topic': 'braindump',
        'editor': os.environ.get('EDITOR', 'vi'),
        'file_ext': '.txt',
    }

    try:
        with open(settings_file if settings_file is not None else os.path.expanduser('~/.braindump')) as f:
            loaded_settings = json.load(f)
    except IOError:
        if settings_file is not None:
            sys.exit('braindump: Unable to load settings file \'{0}\''.format(settings_file))
        loaded_settings = {}

    settings = dict(default_settings.items() + loaded_settings.items())
    settings['braindump_dir'] = os.path.expanduser(settings['braindump_dir'])

    return settings


def main():
    arguments = docopt(__doc__, version=__version__)
    settings = load_settings(arguments['--settings'])

    dumper = FSDumper(settings)
    topic = arguments['TOPIC'] if arguments['TOPIC'] is not None else settings['default_topic']

    if arguments['ls'] is True:
        topics = dumper.list_topics()
        output = '{0} braindump topics:'.format(len(topics))
        for topic in topics:
            output += '\n- {0}'.format(topic)
        print output
    elif arguments['-m'] is not None:
        dumper.quick_add(topic, arguments['-m'])
    else:
        dumper.edit_topic(topic)
