import requests
from bs4 import BeautifulSoup

# Base URL of the archive search
USER = "thewitchking"
BASE_URL = "https://desuarchive.org/r9k/search/username/{}/".format(USER)
OUTPUT_FILE = "posts.txt"

def get_posts_from_page(page_url):
    """
    Fetches and parses posts from a single page.
    """
    try:
        response = requests.get(page_url)
        response.raise_for_status()  # Check for HTTP request errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all posts
        posts = soup.find_all("blockquote", class_="postMessage")
        post_texts = [post.get_text(strip=True) for post in posts]
        return post_texts
    except Exception as e:
        print(f"Error fetching {page_url}: {e}")
        return []

def scrape_all_posts():
    """
    Scrapes all posts by navigating through paginated results.
    """
    all_posts = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        page_url = f"{BASE_URL}?page={page}"
        posts = get_posts_from_page(page_url)

        if not posts:
            print("No more posts found or end of pages reached.")
            break

        all_posts.extend(posts)
        page += 1

    return all_posts

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
    print("Starting scraping...")
    posts = scrape_all_posts()
    if posts:
        save_to_file(posts, OUTPUT_FILE)
    else:
        print("No posts scraped.")
