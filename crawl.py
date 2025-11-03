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
	elif p_tag:
		if soup.p.string == None:
			return ""
		return soup.p.string
	else:
		return ""

def get_urls_from_html(html, base_url):
	soup = BeautifulSoup(html, 'html.parser')
	result_arr = []
	a_tags = soup.find_all("a", href = True)
	if a_tags:
		for a in soup.find_all("a", href = True):
			if "http" in  a["href"]:
				result_arr.append(a["href"])
			else:
				result_arr.append(f"{base_url}{a["href"]}")
		return result_arr
	else:
		return result_arr


def get_images_from_html(html, base_url):
	soup = BeautifulSoup(html, 'html.parser')
	result_arr = []
	img_tags = soup.find_all("img")
	if img_tags:
		for img in soup.find_all("img", src = True):
			
			if "http" in  img["src"]:
				result_arr.append(img["src"])
			else:
				result_arr.append(f"{base_url}{img["src"]}")
		return result_arr
	else:
		return result_arr
	


def extract_page_data(html, page_url):
	p = get_first_paragraph_from_html(html)
	h1 = get_h1_from_html(html)
	a = get_urls_from_html(html, page_url)
	img = get_images_from_html(html, page_url)
	obj = {
		"url": page_url,
        "h1": h1,
        "first_paragraph": p,
        "outgoing_links": a,
        "image_urls": img,

	}
	return obj