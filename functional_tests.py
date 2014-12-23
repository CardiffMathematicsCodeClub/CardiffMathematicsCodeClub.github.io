from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://0.0.0.0:4000/')

assert 'Cardiff School of Mathematics Code Club' in browser.title
