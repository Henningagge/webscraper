import unittest
from crawl import normalize_url
from crawl import get_h1_from_html
from crawl import get_first_paragraph_from_html
from crawl import get_urls_from_html
from crawl import get_images_from_html
from crawl import extract_page_data
class TestCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https//:blog.boots.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boots.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_path(self):
        input_url = "http//:blog.boots.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boots.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_pathdash(self):
        input_url = "http//:blog.boots.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boots.dev/path"
        self.assertEqual(actual, expected)

    def test_normalize_urldash(self):
        input_url = "https//:blog.boots.dev/path/"
        actual = normalize_url(input_url)
        expected = "blog.boots.dev/path"
        self.assertEqual(actual, expected)

    def test_h1_html(self):
        input_html = "<h1>Hello World</h1>"
        actual = get_h1_from_html(input_html)
        expected = "Hello World"
        self.assertEqual(actual, expected)

    def test_h1_htmlempty(self):
        input_html = "<h1></h1>"
        actual = get_h1_from_html(input_html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_h1_htmlfalsetag(self):
        input_html = "<p>hello world</p>"
        actual = get_h1_from_html(input_html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_h1_htmlfalsetag(self):
        input_html = "<html><body><h1>Test Title</h1></body></html>"
        actual = get_h1_from_html(input_html)
        expected = "Test Title"
        self.assertEqual(actual, expected)



    def test_first_paragraph_from_htmlnormal(self):
        input_html = "<p>hello world</p>"
        actual = get_first_paragraph_from_html(input_html)
        expected = "hello world"
        self.assertEqual(actual, expected)

    def test_first_paragraph_from_htmlempty(self):
        input_html = "<p></p>"
        actual = get_first_paragraph_from_html(input_html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_first_paragraph_from_htmlnone(self):
        input_html = "<h1>hello</h1>"
        actual = get_first_paragraph_from_html(input_html)
        expected = ""
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = '''<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
            </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)



    def test_urls_from_html(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)

    def test_urls_from_htmlnew(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="/hello"><span>Boot.dev/hello</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/hello"]
        self.assertEqual(actual, expected)
    
    def test_urls_from_htmlblock(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="/cool.html"><span>Boot.dev.nice</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/cool.html"]
        self.assertEqual(actual, expected)
    
    def test_urls_from_htmlref(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://hello.com"><span>Hello.com</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://hello.com"]
        self.assertEqual(actual, expected)

    def test_urls_from_htmlmul(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://hello.com"><span>Hello.com</span></a>' \
        '<a href="https://morning.com"><span>Moor.com</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://hello.com", "https://morning.com"]
        self.assertEqual(actual, expected)
    
    def test_urls_from_htmlnone(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

    def test_image_from_html(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/logo.png"]
        self.assertEqual(actual, expected)

    def test_image_from_htmlmul(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><img src="/logo.png" alt="Logo"><img src="/pokemon.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/logo.png", "https://blog.boot.dev/pokemon.png"]
        self.assertEqual(actual, expected)
    
    def test_image_from_htmlnone(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)


    def test_extract_page_data_basic(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <a href="/link1">Link 1</a>
            <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "https://blog.boot.dev",
            "h1": "Test Title",
            "first_paragraph": "This is the first paragraph.",
            "outgoing_links": ["https://blog.boot.dev/link1"],
            "image_urls": ["https://blog.boot.dev/image1.jpg"]
        }
        self.assertEqual(actual, expected)
    
    def test_extract_page_data_basicnolink(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "https://blog.boot.dev",
            "h1": "Test Title",
            "first_paragraph": "This is the first paragraph.",
            "outgoing_links": [],
            "image_urls": ["https://blog.boot.dev/image1.jpg"]
        }
        self.assertEqual(actual, expected)
    
    def test_extract_page_data_basicnoimg(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
            <h1>Test Title</h1>
            <p>This is the first paragraph.</p>
            <a href="/link1">Link 1</a>
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
            "url": "https://blog.boot.dev",
            "h1": "Test Title",
            "first_paragraph": "This is the first paragraph.",
            "outgoing_links": ["https://blog.boot.dev/link1"],
            "image_urls": []
        }
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()
