import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://cloudmonitor.console.aliyun.com')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime())
print('在', current_time, '退出监控')
driver.delete_all_cookies()
driver.quit()
