#
# This program does a Google search for video for "Iron Maiden" and returns
# 50 results. Video search requires NLTK. For instruction on installation please visit http://www.nltk.org/install.html
#

from xgoogle.search import GoogleVideoSearch, SearchError
try:
    gs = GoogleVideoSearch("Iron Maiden")
    gs.results_per_page = 50
    results = gs.get_results()
    for res in results:
        print 'Name: ' + res.name.encode('utf8')
        print 'URL: ' + res.url.encode('utf8')
        print 'Date: ' + res.date.encode('utf8')
        print 'Duration: ' + res.duration.encode('utf8')
        print 'Author: ' + res.author.encode('utf8')
        print 'Description: ' + res.description.encode('utf8')
        
        print
except SearchError, e:
    print "Search failed: %s" % e

