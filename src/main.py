from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import getpass
import pyperclip


print(r"""
                                                                                       $$\                         
                                                                                       $$ |                        
 $$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$  _____|$$  __$$\ $$  __$$\  \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |  \__|$$$$$$$$ |$$ /  $$ |$$ /  $$ |      $$ /      $$ |  \__|$$$$$$$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |      $$   ____|$$ |  $$ |$$ |  $$ |      $$ |      $$ |      $$   ____|$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
$$ |      \$$$$$$$\ $$$$$$$  |\$$$$$$  |      \$$$$$$$\ $$ |      \$$$$$$$\ \$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
\__|       \_______|$$  ____/  \______/        \_______|\__|       \_______| \_______|  \____/  \______/ \__|      
                    $$ |                                                                                           
                    $$ |                                                                                           
                    \__|                                                                                                                                                                                     
""")

options = Options()
options.headless = True

try:
    browser = webdriver.Chrome(
        options=options, executable_path="C:/selenium/chromedriver.exe")
except WebDriverException:
    print("Install Google Chrome for create-repo to work...")
    print("Trying Firefox 🦊")
    browser = webdriver.Firefox(
        options=options, executable_path="C:/selenium/geckodriver.exe")

browser.get("https://github.com/login")

try:
    username = browser.find_element_by_name("login")
    password = browser.find_element_by_name("password")
    sign_in = browser.find_element_by_name("commit")
    
    uname = input("Enter username/email : ").rstrip()
    username.send_keys(uname)

    pwd = getpass.getpass("Enter password : ")
    password.send_keys(pwd)

    sign_in.click()

    if browser.title == 'GitHub':
        browser.get("https://github.com/new")

        repo_name = input("\nEnter repository name (you want to create) : ")
        browser.find_element_by_id("repository_name").send_keys(repo_name)

        repo_description = input("\nEnter description : ")
        browser.find_element_by_id(
            "repository_description").send_keys(repo_description)

        privacy = True if int(
            input("\nEnter 1 for private, 0 for public repository : ")) == 1 else False
        if privacy:
            browser.find_element_by_xpath("//*[@value = 'private']").click()
        else:
            browser.find_element_by_xpath("//*[@value = 'public']").click()

        readme_init = True if int(
            input("\nEnter 1 initializing repository with readme : ")) == 1 else False
        if readme_init:
            browser.find_element_by_xpath(
                "//*[@id='repository_auto_init']").click()

        print("Doing Magic 🪄")

        create_repo = browser.find_elements_by_css_selector(
            "button.btn:nth-child(12)")[0]
        create_repo.click()

    else:
        print("Error logging in !")


except NoSuchElementException:
    print("Error occured. Please enter correct details.")

else:
    github_repo_link_https = "https://github.com/" + uname + "/" + repo_name + ".git"
    github_repo_link_ssh = "git@github.com:" + uname + "/" + repo_name + ".git"

    print("\n1. HTTPS - {}".format(github_repo_link_https))
    print("2. HTTPS - {}".format(github_repo_link_ssh))

    link = int(input(
        "If you want in clipboard,\nPress 1 for HTTPS, 2 for SSH Github Repo Link : "))
    if link == 1:
        pyperclip.copy(github_repo_link_https)
    elif link == 2:
        pyperclip.copy(github_repo_link_ssh)

    print("\nLink is copied on Clipboard.")