#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import errno
import shutil
import sys

from braindump.dumpers import FSDumper

BRAINDUMP_TEST_DIR = os.path.expanduser(os.environ.get('BRAINDUMP_TEST_DIR', '/tmp/braindump'))

if os.path.isdir(BRAINDUMP_TEST_DIR) and os.listdir(BRAINDUMP_TEST_DIR) != []:
    sys.exit('braindump test dir exists and is not empty. This directory is destroyed and recreated several times during testing; aborting test suite.')


class FSDumperTestCase(unittest.TestCase):
    def setUp(self):
        try:
            os.makedirs(BRAINDUMP_TEST_DIR)
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

        self.settings = {
            'braindump_dir': BRAINDUMP_TEST_DIR,
            'file_ext': '.txt',
        }
        self.dumper = FSDumper(self.settings)

    def tearDown(self):
        shutil.rmtree(BRAINDUMP_TEST_DIR)

    def test_dumper_topic_filename(self):
        topic = 'test'
        filename = topic + self.settings['file_ext']
        self.assertEqual(self.dumper._get_topic_filename(topic), BRAINDUMP_TEST_DIR + '/' + filename)
        self.assertEqual(self.dumper._get_topic_filename(topic, True), BRAINDUMP_TEST_DIR + '/' + filename)
        self.assertEqual(self.dumper._get_topic_filename(topic, False), filename)

    def test_quick_add(self):
        topic = 'test'
        self.assertEqual(self.dumper.quick_add(topic, 'this is only a test'), True)
        self.dumper.quick_add(topic, 'i repeat, only a test')
        with file(self.dumper._get_topic_filename(topic)) as f:
            self.assertEqual(f.read(), 'this is only a test\ni repeat, only a test\n')

    def test_list_topics(self):
        topics = ['foo', 'bar', 'test']
        for topic in topics:
            self.dumper.quick_add(topic, 'foo')

        topic_list = self.dumper.list_topics()
        topic_list.sort()  # the topic list isn't ordered
        topics.sort()

        self.assertEqual(topic_list, topics)


if __name__ == '__main__':
    unittest.main()
