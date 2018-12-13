from elasticsearch import Elasticsearch


def search(query):
    query_contains = {
        'query': {
            'match': {
                'title': query,
            }
        }
    }
    es = Elasticsearch()
    searched = es.search("tieba_index", doc_type="tiezi", body=query_contains, size=20)

    return searched


for res in search("假期都做什么呢")["hits"]["hits"]:
    print(res["_source"]["title"], res["_score"])
