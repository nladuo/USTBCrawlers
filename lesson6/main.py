from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap['phantomjs.page.settings.userAgent'] = ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
exe_path = "/usr/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=exe_path, desired_capabilities=dcap)

driver.get("https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3")

driver.save_screenshot("screenshot.png")  # 截个图
print(driver.page_source)  # 打印源码

driver.quit()

