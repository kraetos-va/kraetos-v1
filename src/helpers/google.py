from googlesearch import search

# Make Google search query
def googleSearch(query):
    return search(query, num_results=3, lang="en", proxy=None)