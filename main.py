import sys
from crawl import normalize_url, get_urls_from_html, extract_page_data
import requests
from urllib.parse import urlparse
def main():
    
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(sys.argv) >2:
        print("too many arguments provided")
        sys.exit(1)
    
    base_url = sys.argv[1]
    print(f"starting crawl, of: {base_url}")
    
    page = crawl_page(base_url)
    print(f"data is {len(page)} log")
    for site in page.values():
        print(f"{site['url']}")

    sys.exit(0)

def get_html(url):

    try:
        r = requests.get(url , headers={
            "User-Agent": "BootCrawler/1.0"
            })
        if r.status_code >= 400:
            raise Exception ("Error code 400+")
        if r.headers['Content-Type'] != "text/html":
            raise Exception ("wrong content type") 
        print(r.content)
        return r.content
    except Exception as e:
        print(e)
        return (e)

def crawl_page(base_url, current_url=None, page_data=None):
    if current_url is None:
        current_url = base_url
    if page_data is None:
        page_data = {}
    base_url = base_url.urlparse(base_url)
    current_url = current_url.urlparse(current_url)
    if base_url.netloc != current_url.netloc:
        return page_data
    normalized_url = normalize_url(current_url)
    if normalize_url not in page_data:
        html = get_html(current_url)
        html_data = extract_page_data(html)
        page_data[normalized_url] = html_data
        a_tags = get_urls_from_html(html, base_url)
        for a_tag in a_tags:
            crawl_page(base_url, a_tag, page_data)
        return page_data
    else:
        return page_data
if __name__ == "__main__":
    main()
