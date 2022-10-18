from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# exec(open("./init.py").read())

load_dotenv()
USERNAME = os.getenv("usr")
PASSWORD = os.getenv("pswd")

driver = webdriver.Chrome(ChromeDriverManager().install())

def login(url, usernameID, username, passwordID,  password, submitID):
    driver.get(url)
    driver.find_element(By.NAME, usernameID).send_keys(username)
    driver.find_element(By.NAME, passwordID).send_keys(password)
    driver.find_element(By.ID, submitID).click()

def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    classes = soup.find_all("a")
    print(soup)
    print(url)
    


if __name__ == "__main__":
    login("https://millburn.powerschool.com/guardian/home.html", "account", USERNAME, "pw", PASSWORD, "btn-enter-sign-in")
    scrape("https://millburn.powerschool.com/guardian/home.html")

