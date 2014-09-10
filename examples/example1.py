#!/usr/bin/python
#
# This program does a Google search for "quick and dirty" and returns
# 50 results.
#

from xgoogle.search import GoogleSearch, SearchError
try:
  gs = GoogleSearch("game of thrones season 3")
  gs.results_per_page = 50
  results = gs.get_results()
  for res in results:
    print res.title.encode('utf8')
    print res.desc.encode('utf8')
    print res.excerpt.encode('utf8')
    print res.url.encode('utf8')
    print
except SearchError, e:
  print "Search failed: %s" % e

