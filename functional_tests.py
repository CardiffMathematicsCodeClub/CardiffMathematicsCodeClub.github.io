from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_check_the_blog(self):
        # Zoe wants to take a look at the code club site.
        # She opens up the browser at the homepage:
        self.browser.get('http://0.0.0.0:4000/')

        # She checks that the title shows that she's in the correct place.
        assert 'Cardiff School of Mathematics Code Club' in self.browser.title

if __name__ == '__main__':
    #unittest.main(warnings='ignore')
    unittest.main()
