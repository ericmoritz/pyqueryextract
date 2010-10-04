Warning this is a work in progress.  I wouldn't use this for anything that
will kill someone if it fails.

This project defines a really simple JSON based DSL for converting (X)HTML into
dictionaries.  Here is an example::

     >>> from pyquery import PyQuery
     >>> from pyqueryextract import extract
     >>> d = PyQuery('<a href="http://www.google.com/">Google!</a>')
     >>> spec = {'link': {'$query': 'a', '$op': ['attr', 'href']}, 'txt': {'$query': 'a'}}
     >>> print extract(d, spec)
     {'link': 'http://www.google.com/', 'txt': 'Google!'}

