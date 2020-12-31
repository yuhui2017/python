'''
    实现功能：
        利用selenium 监控github某个仓库是否发生更新变化
        如果存在更新，自动打开
'''
#更新
from selenium import webdriver
import time
import requests


path = '/Users/mac/work/python/python_exec/实用主义学python/GitHub/chromedriver'
driver = webdriver.Chrome(executable_path=path)

#仓库名
res_name = 'yuhui2017/python'
#github-api
api = f'https://api.github.com/repos/{res_name}'
#仓库地址
url = f'https://github.com/{res_name}'

old_time = None
while True:

    #利用api中的updated_at属性判断是否发生更新
    r = requests.get(api)
    if r.status_code != 200:
        print(f"{url}访问失败......")
        break

    #r --> dict
    update_time = r.json()['updated_at']

    #如果old_time为空则把当前更新时间赋给他
    if not old_time:
        old_time = update_time
    
    #更新时间发生变化：说明存在更新
    if old_time < update_time:
        print(f'{res_name}存在更新,尝试打开网页')
        driver.get(api)
        old_time = update_time

    time.sleep(120)
