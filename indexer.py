import os,os.path
from whoosh import index
from whoosh.fields import Schema,ID,TEXT,KEYWORD,STORED
from whoosh.analysis import StemmingAnalyzer
from whoosh.qparser import QueryParser
if not os.path.exists("indexdir"):
    os.mkdir("indexdir")
schema = Schema(from_addr=ID(stored=True),path=TEXT(stored=True),to_addr=ID(stored=True),subject=TEXT(stored=True),body=TEXT(analyzer=StemmingAnalyzer(),stored=True))
ix =  index.create_in("indexdir",schema)
fname=open('spam1.txt')
buffer1=fname.readlines()
 
writer=ix.writer()
writer.add_document(subject=u"my first index test",body=u"hello world indexers")

writer.commit()
qp = QueryParser("body",schema=ix.schema)
q = qp.parse(u"family")
with ix.searcher() as searcher:
    results = searcher.search(q)
    results.fragmenter.charlimit = 100000
    print results
    for hit in results:
        print("subject of email: "+hit["subject"])
        print(hit.highlights("body",top=5))
        print(hit["body"])
       # print(hit.highlights("body"))
       # with open(hit["path"]) as fileobj:
        #    filecontents = fileobj.read()
        #print(hit.highlights("body", text=filecontents))

