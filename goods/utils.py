from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

from goods.models import Product


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Product.objects.filter(id=query)

    vector = SearchVector("name", "description")
    query = SearchQuery(query)

    return Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank")