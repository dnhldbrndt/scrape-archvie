import moesearch

USER = "TheWitchKing"
OUTPUT_FILE = "posts.txt"
BOARD = "r9k"

def get_posts(num_posts):
    posts = []
    start = 0

    while len(posts) < num_posts:
        # Fetch the next batch of posts
        results = moesearch.search(
            archiver_url="https://desuarchive.org",
            board=BOARD,
            username=USER,
            limit=100,  # Fetch 100 posts at a time if supported
            offset=start
        )

        # If no results are returned, stop (user might not have enough posts)
        if not results:
            print("No more posts found.")
            break

        # Accumulate comments into the posts list
        posts.extend([post.comment for post in results])

        # Update the offset for pagination
        start += len(results)

    # Ensure we return only the requested number of posts
    return posts[:num_posts]

def save_to_file(posts, filename):
    """
    Saves the list of posts to a text file.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for post in posts:
                f.write(post + "\n")  # Add a newline after each post
        print(f"Posts successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

if __name__ == "__main__":
    print("Start scraping...")
    posts = get_posts(100)
    if posts:
        save_to_file(posts, OUTPUT_FILE)
    else:
        print("No posts scraped.")
