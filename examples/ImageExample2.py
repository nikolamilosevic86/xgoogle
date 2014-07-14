#
# This program does a Google search for images for "quick and dirty" and returns
# 50 results.
#

from xgoogle.search import GoogleImageSearch, SearchError
try:
    gs = GoogleImageSearch("quick and dirty")
    gs.results_per_page = 50
    results = gs.get_results()
    for res in results:
        print res.trumb.encode('utf8')
        print res.url.encode('utf8')
        print
except SearchError, e:
    print "Search failed: %s" % e

