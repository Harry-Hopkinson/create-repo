from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import getpass
import pyperclip

print("")

options = Options()
options.headless = True

try:
    browser = webdriver.Chrome(
        options=options, executable_path="C:/selenium/chromedriver.exe") # do your installation path

except WebDriverException:
    browser = webdriver.Firefox(
        options=option, executable_path="C:/selenium/geckodriver.exe")

browser.get("https://github.com/login")