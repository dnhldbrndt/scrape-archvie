import moesearch

if __name__ == "__main__":
    print(moesearch.search(archiver_url="https://desuarchive.org", board="a", username="Test")[1].comment)