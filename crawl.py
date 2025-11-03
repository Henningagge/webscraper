from urllib.parse import urlparse
from bs4 import BeautifulSoup
def normalize_url(url):
	parsed_url = urlparse(url)
	full_path = f"{parsed_url.netloc}{parsed_url.path}"
	full_path = full_path.rstrip("/")
	path = 	full_path.split(":")
	return path[1].lower()
def get_h1_from_html(html):
	soup = BeautifulSoup(html, 'html.parser')
	h1_tag = soup.find("h1")
	if h1_tag:
		if soup.h1.string == None:
			return ""
		return soup.h1.string
	else:
		return ""
def get_first_paragraph_from_html(html):
	soup = BeautifulSoup(html, 'html.parser')
	p_tag = soup.find("p")
	main_tag = soup.find("main")
	if main_tag:
		if p_tag:
			if soup.main.p.string == None:
				return ""
		return soup.main.p.string
	else:
		return ""

def get_urls_from_html(html, base_url):



def get_images_from_html(html, base_url):