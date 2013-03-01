import sys
from braindump.core import Usage


class QuickAdd(Usage):
    options = [
        ('-m MESSAGE', 'Add a message without opening your editor'),
    ]

    def match(self):
        return self.arguments['-m'] is not None

    def execute(self, dumper, topic):
        if not dumper.quick_add(topic, self.arguments['-m']):
            sys.exit('Unable to append message to dumpfile \'{0}\''.format(topic))
