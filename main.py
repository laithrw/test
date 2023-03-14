from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import urllib.parse
import time
import re
import random
import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



question = "You are math/science assistant. Break explanations into steps, ONLY return valid JSON array (LaTeX for nums) " \
           "in this format: [{'title': 'step_title', 'description': 'step_description'}..., " \
           "{'answer': 'answer'}, {'websites': [url]}]\nQuestion: " + input("Enter your question: ") + "\nJSON Answer: "
if len(question) > 375:
    print("Question is too long. Please try again.")
    exit(1)
encoded_s = urllib.parse.quote_plus(question)

# Create an Options instance and add the argument "headless"
options = Options()
options.add_argument("headless")
start = time.time()

proxies = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt").text
proxies = re.split("\n", proxies)
total_proxies = len(proxies)
random_int = random.randint(0, total_proxies - 1)
proxy = proxies[random_int]
proxy = f"http://{proxy}"  # your specified IP and port
proxy = "http://81.12.44.197:3129/"

# Create a web driver instance with the options parameter and open the webpage
start = time.time()
srv = Service(ChromeDriverManager().install())
ua = UserAgent()
userAgent = ua.random
options = Options()
# options.add_argument('--headless')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument(f'user-agent={userAgent}')
options.add_argument('--proxy-server={}'.format(proxy))
driver = webdriver.Chrome(service=srv, options=options)

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('--disable-gpu')
# chrome_prefs = {}
# options = webdriver.ChromeOptions()
# chrome_prefs["profile.default_content_settings"] = {"images": 2}
# options.experimental_options["prefs"] = chrome_prefs
# driver = webdriver.Chrome(options=options, service=srv)



# waitWebDriver = WebDriverWait(driver, 10)
# driver.get("https://www.iask.ai/?q=" + encoded_s)
driver.get("https://api.ipify.org?format=json")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "prose")))

print("Time taken to load the page: " + str(time.time() - start) + " seconds")

# Get the page source from the web driver and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
response, index, formatted_answer = str(soup.find("div", {"class": "prose"}).get_text().strip()), 0, None
print(response)
# while True:
#     while True:
#         try:
#             if response.find("}", index) == -1:
#                 break
#             formatted_answer = response[response.find("["):response.find("}", index)] + "}]"
#             index += 1
#         except ValueError:
#             break
#     if formatted_answer is not None:
#         print(formatted_answer)
#     if "]" in response:
#         break
#
driver.close()  # close the web driver