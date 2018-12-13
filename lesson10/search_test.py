from elasticsearch import Elasticsearch


def search(query):
    query_contains = {
        'query': {
            'multi_match': {
                'query': query,
                "fields": ["title"]
            }
        }
    }
    es = Elasticsearch()
    searched = es.search("tieba_index", doc_type="tiezi", body=query_contains, size=20)

    return searched


for res in search("德语")["hits"]["hits"]:
    print(res["_source"]["title"], res["_score"])
