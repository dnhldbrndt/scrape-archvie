import moesearch

USER = "TheWitchKing"
OUTPUT_FILE = "posts.txt"

def get_posts(page_url):
    return []

def save_to_file(posts, filename):
    """
    Saves the list of posts to a text file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for post in posts:
                f.write(post + "\n\n")
        print(f"Posts successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

if __name__ == "__main__":
    print("Start scraping...")
    posts = get_posts()
    if posts:
        save_to_file(posts, OUTPUT_FILE)
    else:
        print("No posts scraped.")
