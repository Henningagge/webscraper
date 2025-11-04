import sys
from crawl import  crawl_site_async
import asyncio
from urllib.parse import urlparse
from csv_repor import write_csv_report
async def main():
    
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    elif len(sys.argv) > 4:
        print("too many arguments provided")
        sys.exit(1)
    
    base_url = sys.argv[1]
    print(f"starting crawl, of: {base_url}")
    
    page_data = await crawl_site_async(base_url, sys.argv[2], sys.argv[3])
    print(page_data)
    for page in page_data.values():
        print(f"Found {len(page['outgoing_links'])} outgoing links on {page['url']}")
    csv = write_csv_report(page_data)
    print(csv)
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
