#
# This program does a Google search for face images for "quick and dirty" and returns
# 50 results.
#

from xgoogle.search import GoogleFaceImageSearch, SearchError
try:
    gs = GoogleFaceImageSearch("quick and dirty")
    gs.results_per_page = 50
    results = gs.get_results()
    for res in results:
        print res.trumb.encode('utf8')
        print res.url.encode('utf8')
        print
except SearchError, e:
    print "Search failed: %s" % e

