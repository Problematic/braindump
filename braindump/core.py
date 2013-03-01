class BraindumpException(Exception):
    pass


class Dumper(object):
    def __init__(self, settings, *args, **kwargs):
        self.settings = settings

    def quick_add(self, topic, message):
        raise NotImplementedError()

    def edit_topic(self, topic):
        raise NotImplementedError()

    def list_topics(self):
        raise NotImplementedError()

    def archive_topic(self, topic):
        raise NotImplementedError()


class Usage(object):
    usage = '[options] [--] [TOPIC]'
    options = [
        ('-v --version', 'Show version information'),
        ('-h --help', 'Show this help screen'),
        ('-s --settings SETTINGS_FILE', 'Settings file to load'),
    ]
    priority = 100

    def __init__(self, arguments):
        self.arguments = arguments
