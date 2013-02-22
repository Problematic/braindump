`docopt <https://github.com/docopt/docopt>`_-powered dumping for your brain:

.. code-block:: bash
    $ pip install braindump
    ...
    $ braindump -h
    braindump - record what's on your mind

    Usage:
      braindump archive TOPIC
      braindump ls
      braindump [options] [--] [TOPIC]

    Options:
      -v --version                    Show version information
      -h --help                       Show this help screen
      -s --settings SETTINGS_FILE     Settings file to load
      -m MESSAGE                      Add a message without opening your editor
    $ braindump quotes -m "To be, or not to be... - Hamlet"
    $ cat ~/braindump/quotes.txt
    To be, or not to be... - Hamlet
