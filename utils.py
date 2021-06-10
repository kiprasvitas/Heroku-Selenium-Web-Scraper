import undetected_chromedriver.v2 as uc
import base64
from time import sleep
import os
import asyncio
import requests
import json
import sys


def scrapeWebsite(url):
    
    options = uc.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = uc.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), keep_alive=True, version_main=90, patcher_force_close=True, options=options, enable_cdp_events=True)

    driver.get(url)
    print("website loaded successfully")
    try:
        html = driver.page_source
        driver.quit()
        return html
    except:
        driver.quit()
        return "No website found with this URL."