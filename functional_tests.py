from selenium import webdriver

browser = webdriver.Firefox()


# Zoe wants to take a look at the code club site.
# She opens up the browser at the homepage:
browser.get('http://0.0.0.0:4000/')

# She checks that the title shows that she's in the correct place.
assert 'Cardiff School of Mathematics Code Club' in browser.title

# She clicks on the Blog page

# She then clicks on the Past sessions page

# She then clicks on the project page

# She then takes a look at the inspiration page

# After all this she closes the browser (she now knows everything about code)
browser.close()
