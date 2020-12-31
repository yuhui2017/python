from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#global driver
path = '/Users/mac/work/python/python_exec/实用主义学python/GitHub/chromedriver'
driver = webdriver.Chrome(executable_path=path)
driver.get('https://baidu.com')

#根据页面获取输入框id='kw'
input = driver.find_element_by_id('kw').click()
#清空输入框内容
input.clear()
#输入框输入内容
input.send_keys("jd")
#模拟回车操作
input.send_keys(Keys.ENTER)
 
