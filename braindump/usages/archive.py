from braindump.core import Usage


class Archive(Usage):
    usage = 'archive TOPIC'

    def match(self):
        return self.arguments['archive'] is True

    def execute(self, dumper, topic):
        dumper.archive_topic(topic)
