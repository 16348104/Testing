# coding=utf-8
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# driver = webdriver.Firefox()
driver = webdriver.Chrome()  # windows
# driver = webdriver.Chrome(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # mac  chrome
# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/geckodriver')  # mac  firefox
print("======登录阿里云监控=====")
print('测试浏览器:' + driver.name)
driver.get('https://cloudmonitor.console.aliyun.com')
driver.maximize_window()
time.sleep(5)
driver.switch_to.frame('alibaba-login-box')  # 切入框架
driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
time.sleep(3)
date = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/div[2]/p').text
print(date)
# time.sleep(4)
# print(driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/div[2]/p').text)
driver.switch_to.default_content()
time.sleep(8)
# driver.find_element_by_css_selector(
#     'body > div.viewframeContainer > div.aliyun-console-help-guide > div.help-guide-step.help-guide-step-1 > div.help-guide-step-header > button > i').click()
print('站点监控')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.2020520111.aliyun_sidebar.aliyun_sidebar_cms.6ff9d103iaAGn8#/home/ecs')
time.sleep(4)
print('站点管理')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.12818093.aliyun_sidebar.aliyun_sidebar_cms.488716d0VtQA3i#/newSite/list/')
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'网络学堂应用服务监控2')]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@class='icon-collapse-left']").click()
time.sleep(5)
print('可用率截图')
# driver.save_screenshot('/Users/xdx/Desktop/Monitor.png')  # mac
driver.save_screenshot('D:/Monitor1.png')
time.sleep(2)
print('响应时间截图')
driver.find_element_by_xpath("//div[@class='col-sm-12 margin-top']//div[@class='margin-top chart-style']").click()
time.sleep(2)
# driver.save_screenshot('/Users/xdx/Desktop/Monitor.png')  # mac
driver.save_screenshot('D:/Monitor2.png')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print('程序于', current_time, '退出cloudmonitor')
# os.system('E:/WebDriver--Python/Example/Email/send_mail2.py')
driver.delete_all_cookies()
print('关闭浏览器，删除cookie')
time.sleep(1)
driver.quit()

##发邮件
print('去发邮件!')
# 发送邮件服务器
smtpsever = 'smtp.126.com'
# 用户名密码
# password = input("input:")
password = ''
user = 'xiaodaxing@126.com'
# 发件箱
sender = 'xiaodaxing@126.com'
# 收件箱
receiver = ['47283875@qq.com', 'wlxt@tsinghua.edu.cn']
# 邮件主题
subject = '阿里云监控截图'

# 如名字所示Multipart就是分多个部分
msgRoot = MIMEMultipart()
msgRoot['Subject'] = subject
msgRoot['From'] = user
# HTML类型邮件正文
# msgRoot = MIMEText('<html><h3>Python Mail</h3></html>', 'html', 'utf-8')
att = MIMEText('此为系统测试邮件，请勿直接回复！', 'plain', 'utf-8')
msgRoot.attach(att)
# 邮件附件部分1
sendfile = open('D:/Monitor1.png', 'rb').read()  # windows
# sendfile = open('/Users/xdx/Desktop/Monitor.png', 'rb').read()  # mac
att = MIMEText(sendfile, 'png', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Monitor1.png"'
msgRoot.attach(att)
# 邮件附件部分2
sendfile = open('D:/Monitor2.png', 'rb').read()  # windows
# sendfile = open('/Users/xdx/Desktop/Monitor.png', 'rb').read()  # mac
att = MIMEText(sendfile, 'png', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Monitor2.png"'
msgRoot.attach(att)

try:
    smtp = smtplib.SMTP()
    smtp.set_debuglevel(1)
    smtp.connect(smtpsever, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()
    print('Success,Email has send out!')
except smtplib.SMTPException as e:
    print("error", e)
