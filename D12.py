from selenium import webdriver
from PIL import Image
import time, smtplib, selenium
#import os, sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import ddddocr
from selenium.webdriver.support.ui import Select
from util import *
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
la = '2616220080'
lc = 'Fjsy@150232'
options = Options()
options.add_argument('-headless')
# 打开chrome浏览器
driver = get_web_driver()
#driver = webdriver.Chrome()
# 进入健康情况填报官网
driver.get(r'https://xg.fjsdxy.com/SPCP/Web')
# 最大化窗口
driver.maximize_window()
    # 登录信息
username = driver.find_element(By.XPATH,'//*[@id="StudentId"]')
stu_number = la
username.send_keys(stu_number)
print('登录中')
#try:
    #driver.find_element(By.XPATH,'//*[@id="platfrom2"]').click()
    #driver.find_element(By.XPATH,'//*[@id="platfrom1"]/a/img')  # 尝试获取填体温页面 成功即登录成功
    #print('登录成功')
#except:
namess = driver.find_element(By.XPATH, '//*[@id="codeInput"]')
namess.clear()
stu_password = lc
password = driver.find_element(By.XPATH, '//*[@id="Name"]')
password.send_keys(stu_password)
driver.save_screenshot("2.png")#获取页面截图
img = Image.open('2.png') ## 打开2.png文件，并赋值给img
region = img.crop((1091,343,1173,366))#对获取的截图进行裁剪
region.save('3.png')#保存裁剪后的图片
ocr = ddddocr.DdddOcr()#导入验证码识别
with open("3.png", "rb") as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)#将识别出来的验证码赋给res
print(res)
name = driver.find_element(By.XPATH,'//*[@id="codeInput"]')
number = res
name.send_keys(number)
driver.find_element(By.XPATH, '//*[@id="Submit"]').click()
print('1')
driver.quit()