from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import getpass
import pyperclip

print("")

options = Options()
options.headless = True

try:
    print('Hello World')

except:
    print('Come back to late')