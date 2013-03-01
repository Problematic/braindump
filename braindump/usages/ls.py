from braindump.core import Usage


class Ls(Usage):
    usage = 'ls'

    def match(self):
        return self.arguments['ls'] is True

    def execute(self, dumper, topic):
        topics = dumper.list_topics()
        output = '{0} braindump topics:'.format(len(topics))
        for topic in topics:
            output += '\n- {0}'.format(topic)
        print output
