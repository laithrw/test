from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# SCRAPER_API = os.environ.get("SCRAPER_API")
# PROXY = f'http://scraperapi:{SCRAPER_API}@proxy-server.scraperapi.com:8001'
proxy = "http://200.105.215.22:33630"

srv = Service(ChromeDriverManager().install())
ua = UserAgent()
userAgent = ua.random
options = Options()
options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

chrome_prefs = {}
chrome_prefs["profile.default_content_settings"] = {"images": 2}
options.experimental_options["prefs"] = chrome_prefs

options.add_argument(f'user-agent={userAgent}')
options.add_argument('--proxy-server={}'.format(proxy))
options.add_argument("--disable-webrtc")  # disable WebRTC
options.add_argument("--disable-bundled-ppapi-flash")  # disable Flash
options.add_argument("--disable-javascript")  # disable JavaScript
driver = webdriver.Chrome(service=srv, options=options)
start = time.time()
driver.get("https://iask.ai/?q=What")
print(f"Time taken: {time.time() - start}")
soup = BeautifulSoup(driver.page_source, "html.parser")
print(str(soup.find("div", {"class": "prose"}).get_text().strip()))
driver.quit()