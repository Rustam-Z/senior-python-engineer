import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


if __name__ == "__main__":
    html_page_dir = '/'.join(os.path.dirname(os.path.abspath(__file__)).split("/")[:-1])
    url = "file:///" + html_page_dir + "/html/test.html"
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    try:
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        # Implicit wait
        # google_link1 = driver.find_elements(By.LINK_TEXT, "Google")[0]
        # google_link1.click()

        # Explicit wait
        google_link2 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Google")))
        google_link2.click()

    except Exception as e:
        print("Error: ", e)
    finally:
        time.sleep(2)
        driver.quit()
        print("Test completed")
