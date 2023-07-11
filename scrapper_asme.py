from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os


def asme_active(str):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(
    #     executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options
    # )

    driver = webdriver.Chrome()
    driver.get("https://caconnect.asme.org/directory/")
    elem = WebDriverWait(driver, timeout=150).until(
        lambda d: d.find_element(By.ID, "company-name")
    )
    elem.clear()
    elem.send_keys(str)
    elem.send_keys(Keys.RETURN)

    elem = WebDriverWait(driver, timeout=60).until(
        lambda d: d.find_element(By.CLASS_NAME, "flex-grid")
    )

    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = []
    table_selector = soup.find("div", class_="flex-grid")
    rows_selector = table_selector.find_all("div", class_="item-row")
    for row in rows_selector:
        divs = row.find_all("div")
        r = []
        for div in divs:
            text = div.get_text()
            r.append(text.strip())
        data.append(r)

    for r in data:
        if str in r:
            return True
    return False
