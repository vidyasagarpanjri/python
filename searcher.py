from whoosh import index,qparser
ix = index.open_dir('EmailIndexDir')
while True:
    choice = unicode(raw_input("enter the word u wan to search:"))
    qp = qparser.QueryParser("body",ix.schema)
    q = qp.parse(choice) # word to search
    with ix.searcher() as searcher:
        results= searcher.search(q)
        counter = 0
        print len(results)
        for hit in results:
            counter=counter+1
            print counter
            print "Suject : "+hit["subject"]
            print "Date:"+hit["date"]
            print "From:"+hit["sender"]
            print "Delivered To:"+hit["deli_to"]
            print "Authorisation Result:"+hit["autho_res"]
            print "Bounces To:"+hit["bounces_to"]
            print "content :"+hit["body"]
    pass
    
