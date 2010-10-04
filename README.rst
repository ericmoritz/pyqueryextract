Warning this is a work in progress.  I wouldn't use this for anything that
will kill someone if it fails.

This project defines a really simple JSON based DSL for converting (X)HTML into
dictionaries.  Here is an example::

     from pyquery import PyQuery
     from pyqueryextract import extract
     d = PyQuery('<a href="http://www.google.com/">Google!</a>')
     spec = {
         'hardcoded': 'text',
         'txt':  {'$query': 'a'},
         'link': {'$query': 'a', '$op': ['attr', 'href']},
     }

     data = extract(d, spec)

This would produce the following dictionary::

     {'link': 'http://www.google.com/', 'txt': 'Google!', 'hardcoded': 'text'}

This Equivelent to the following Python code::

     data = {}
     data['hardcoded'] = 'text'
     data['link'] = d("a").attr("href")
     data['txt'] = d("a").text()
     print data

While the python code is much more concise, pyqueryextract specs can be stored wherever 
JSON can be stored.


Explaination
============

At the moment there is only operation defined which is `$query`.  The value it is set to is what will be searched
for in the document.  If `$op` is also defined, it will call the function named in index zero.  For instance, `attr`.
The remaining items  in the `$op` list will be applied to the function name.
