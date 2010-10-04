from pyqueryextract import base
from pyqueryextract import extract
from pyquery import PyQuery
import unittest

content = """
<!-- this is some janky HTML, it's to make sure this works on non-XHTML -->
<html>
  <body>
    <h1>Test Content</h1>

  <ul>
    <li><a href="/somewhere/">Somewhere</a>
    <li><a href="/somewhere-else/">Somewhere Else</a>
"""

class TestQueryOp(unittest.TestCase):
    def test_query_op_simple(self):
        d = PyQuery(content)

        spec = {"$query": "h1"}
        
        expect = "Test Content"
        
        result = base.query_op(d, spec)
        
        self.assertEqual(expect, result)

    def test_query_op_attr(self):
        d = PyQuery(content)

        spec = {"$query": "a",
                "$op": ["attr", "href"]
                }
        
        expect = ["/somewhere/", "/somewhere-else/"]
        
        result = base.query_op(d, spec)
        
        self.assertEqual(expect, result)

        
class TestExecute(unittest.TestCase):
    def test_execute(self):
        d = PyQuery(content)

        spec = {
            'header': {'$query': 'h1'},
            'links': {'$query': 'li a',
                     '$op': ['attr', 'href']}
            }
        
        expect = {
            'header': 'Test Content',
            'links': ['/somewhere/', '/somewhere-else/']
            }

        result = base.extract(d, spec)
        
        self.assertEqual(expect, result)
