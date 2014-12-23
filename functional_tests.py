from selenium import webdriver

browser = webdriver.Firefox()

assert 'Cardiff School of Mathematics Code Gathering' in browser.title
