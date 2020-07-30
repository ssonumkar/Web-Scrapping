from bs4 import BeautifulSoup
from selenium import webdriver
from constants import EVENTS_JSON_LOC ,ROOT_DIR
import os
class Manage_Source_Code:
    def __init__(self):
        pass
    @classmethod
    def get_source_code(cls,url,user_name,passwd):
        # browser = webdriver.Firefox(os.path.join(ROOT_DIR,'geckodriver.exe')) #if browser is firefox
        browser = webdriver.Chrome(os.path.join(ROOT_DIR, 'chromedriver.exe'))  # register browser driver
        browser.get(url)
        # for authentication
        username = user_name  # write username
        password = passwd  # change the password to login jasper

        # Setting the value of username input field
        browser.execute_script(f'var element = document.getElementById("os_username"); element.value = "{username}";')

        # Setting the value of password input field
        browser.execute_script(f'var element = document.getElementById("os_password"); element.value = "{password}";')
        # click the login button also
        browser.execute_script(f'document.getElementById("loginButton").click();')
        return browser.page_source #get the source code

    @classmethod
    def get_table(cls,html,tag,class_name,table_no_in_page):
        soup = BeautifulSoup(html,features="lxml" )
        return soup.find_all(tag, class_=class_name)[table_no_in_page]

    @classmethod
    def get_rows(cls, table):
        return table.find_all("tr")

    @classmethod
    def get_hyperlink(cls, row):
        try:
            a = row.select('a')[0]
            if a['href'].startswith("http"):
                return a['href'] #already present
            return "{}{}".format(a['data-base-url'],a['href'][4:]) #generate hyper link
        except:
            return "" #field empty

    @classmethod
    def extract_date_and_time(cls, combined_date):
        if combined_date != "":
            return {"date": combined_date.split(" ")[0], "time": "".join(combined_date.split(" ")[1:])if len(combined_date.split(" ")) > 1 else ""}
        return {"date": "","time": ""}
