class BraindumpException(Exception):
    pass


class Dumper(object):
    def __init__(self, settings):
        self.settings = settings

    def quick_add(self, topic, message):
        raise NotImplementedError()

    def edit_topic(self, topic):
        raise NotImplementedError()

    def list_topics(self):
        raise NotImplementedError()

    def archive_topic(self, topic):
        raise NotImplementedError()
