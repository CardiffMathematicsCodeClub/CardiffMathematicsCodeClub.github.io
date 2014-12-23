from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_read_the_home_page(self):
        # Zoe wants to take a look at the code club site.
        # She opens up the browser at the homepage:
        self.browser.get('http://0.0.0.0:4000/')
        self.browser.implicitly_wait(3)

        # She checks that the title shows that she's in the correct place.
        self.assertIn('Cardiff School of Mathematics Code Club', self.browser.title)

        # She checks that the header also says Code club:
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Cardiff School of Mathematics Code Club', header_text)

    def test_can_click_on_blog(self):
        # Thomas want to read the blog page from the homepage
        # He open the browser at the blog page
        self.browser.get('http://0.0.0.0:4000/')
        self.browser.implicitly_wait(3)


        # He finds the link to the blog
        link = self.browser.find_element_by_link_text('blog')
        # He clicks on the link
        link.click()
        self.browser.implicitly_wait(3)

        # He checks that the correct url is located
        self.assertEquals('http://0.0.0.0:4000/blog/', self.browser.current_url)

        # He checks that the title shows that he's in the correct place
        self.assertIn('Code Club Blog', self.browser.title)

        # He then checks that the correct header is in place
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Code Club Blog', header_text)

if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
