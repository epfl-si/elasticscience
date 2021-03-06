from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search, Q
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()


class PublicationIndex(DocType):
    title = Text()
    doi = Text()
    pub_date = Date()
    authors = Text()


def bulk_indexing():
    PublicationIndex.init(index='publications')  # Maps the model to ES.
    es = Elasticsearch()

    # Indexes every record in ES.
    bulk(client=es, actions=(b.indexing() for b in
                             models.Publication.objects.all().iterator()))


def search_partial(author):
    return Search(index='publications').query('wildcard', authors='*%s*' % author.lower()).execute().hits.hits


def search_exact(author):
    return Search(index='publications').query('match', authors='%s' % author).execute().hits.hits
