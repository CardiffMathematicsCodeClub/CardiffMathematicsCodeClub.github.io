from selenium import webdriver
from itertools import izip
import unittest
import yaml

class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()


class NewVisitorTest(VisitorTest):

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

    def test_that_have_correct_num_of_contributors(self):
        # Bob wants to see who contributed to the website
        # He opens up the browser at the homepage:
        self.browser.get('http://0.0.0.0:4000/')
        self.browser.implicitly_wait(3)

        # He looks at all the contributors
        contributors = self.browser.find_elements_by_class_name('contributor')

        # He checks that the number of contributor's is the same as in the database
        data_file = open('./_data/contributors.yml', 'r')
        contributor_in_data = yaml.load(data_file)
        data_file.close()
        self.assertEqual(len(contributors), len(contributor_in_data))


class BlogReaderTest(VisitorTest):

    def test_can_click_on_blog(self):
        # Thomas wants to read the blog page from the homepage
        # He open the browser at the home page
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

    def test_that_can_click_on_all_blog_posts(self):
        # Pauline wants to read every blog post
        # She open the browser at the blog page
        self.browser.get('http://0.0.0.0:4000/blog/')
        self.browser.implicitly_wait(3)

        # She finds all links
        links = self.browser.find_elements_by_class_name('post-link')

        # She finds all urls to blog post
        urls = [link.get_attribute("href") for link in links]

        # She reads all the titles
        titles = [link.text for link in links]

        # She then clicks on every link and checks that the title is correct and in the header
        for url, title in izip(urls, titles):
            # She goes to the url
            self.browser.get(url)
            self.browser.implicitly_wait(3)

            # She checks the browser title
            self.assertEqual(title, self.browser.title)
            # She reads the header and checks that it is correct
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertEqual(title, header_text)

            # She click on the Blog header to return to list of blog posts

            link = self.browser.find_element_by_link_text('Blog')
            link.click()


class PastSessionsReaderTest(VisitorTest):

    def test_can_click_on_past_sessions(self):
        # Julien wants to take a look at the past sessions page
        # He opens up the browser at the homepage:
        self.browser.get('http://0.0.0.0:4000/')
        self.browser.implicitly_wait(3)

        # He finds the link to the past sessions page
        link = self.browser.find_element_by_link_text('Past Sessions')
        # He clicks on the link
        link.click()
        self.browser.implicitly_wait(3)

        # He checks that the correct url is located
        self.assertEquals('http://0.0.0.0:4000/sessions.html', self.browser.current_url)

        # He checks that the title shows that he's in the correct place
        self.assertIn('Past Sessions', self.browser.title)

        # He then checks that the correct header is in place
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Past Sessions', header_text)

    def test_that_have_correct_number_of_session(self):
        # Meryl wants to read through the past session quotes
        # She opens up the browser at the past session page
        self.browser.get('http://0.0.0.0:4000/sessions.html')
        self.browser.implicitly_wait(3)

        # She looks at all the quotes
        quotes = self.browser.find_elements_by_class_name('session-quote')

        # She checks that the number of quotes is the same as in the database
        data_file = open('./_data/past_sessions.yml', 'r')
        quotes_in_data = yaml.load(data_file)
        data_file.close()
        self.assertEqual(len(quotes), sum([len(i['sessions']) for i in quotes_in_data]))


if __name__ == '__main__':
    unittest.main()
