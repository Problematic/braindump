from __future__ import print_function

import sys
import os
from subprocess import call, Popen
from glob import glob


class FSDumper(object):
    def __init__(self, settings):
        if not os.access(settings['braindump_dir'], os.W_OK | os.X_OK):
            sys.exit('braindump: couldn\'t access braindump dir \'{0}\'. Does it exist/is it writable?'.format(settings['braindump_dir']))

        self.settings = settings

    def quick_add(self, topic, message):
        filename = self._get_topic_filename(topic)
        try:
            with open(filename, mode='a') as f:
                print(message, file=f)
        except IOError:
            sys.exit('Unable to append message to dumpfile \'{0}\''.format(filename))

    def edit_topic(self, topic):
        self._launch_editor(self.settings['editor'], self._get_topic_filename(topic))

    def list_topics(self):
        topic_files = glob('{0}/*{1}'.format(self.settings['braindump_dir'], self.settings['file_ext']))
        topics = []
        for topic in topic_files:
            topics.append(os.path.splitext(os.path.basename(topic))[0])
        return topics

    def _get_topic_filename(self, topic, full=True):
        filename = topic + self.settings['file_ext']

        if full is True:
            return os.path.join(self.settings['braindump_dir'], filename)

        return filename

    def _launch_editor(self, editor, filename, wait=True):
        shell_string = '{0} "{1}"'.format(editor, filename)
        if wait is True:
            exit_code = call(shell_string, shell=True)
            return exit_code
        else:
            Popen([shell_string], shell=True)
