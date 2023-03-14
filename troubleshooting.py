from selenium import webdriver
options = webdriver.FirefoxOptions()
proxy = 'http://192.111.134.10:4145'
options.add_argument('--proxy-server=socks5://' + proxy)
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.socks_remote_dns", True)
profile.set_preference("network.proxy.socks_version", 5)
driver = webdriver.Firefox(options=options, firefox_profile=profile)
driver.get("https://api.ipify.org")
print(driver.page_source)