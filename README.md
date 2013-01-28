[docopt](https://github.com/docopt/docopt)-powered dumping for your brain

### pip install braindump

```
$ braindump -h
braindump - record what's on your mind

Usage:
    braindump ls
    braindump [options] [--] [TOPIC]

Arguments:
    ls                              Output a list of topic files
    TOPIC                           Subject to braindump on, determines filename [default: braindump]

Options:
    -v --version                    Show version information
    -h --help                       Show this help screen
    -s --settings SETTINGS_FILE     Settings file to load
    -m MESSAGE                      Add a message without opening your editor
$ braindump quotes -m "To be, or not to be... - Hamlet"
$ cat ~/braindump/quotes.txt
To be, or not to be... - Hamlet
```
