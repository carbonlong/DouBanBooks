# -*- coding: utf-8 -*-

from typing import Callable
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
import time, random
import openpyxl

""" Requirement Pyhton3
pip install selenium==4.9.1
pip install openpyxl==3.1.2
"""

def web_driver() -> WebDriver:
    # 配置 ChromeDriver 的路径 要和电脑上面的chrome浏览器版本对应
    # 下载地址 https://npm.taobao.org/mirrors/chromedriver/
    # chromedriver_path = 'user_path/chromedriver'
    chromedriver_path = './chromedriver.exe'
    # 创建 ChromeDriver 选项
    chrome_options = Options()
    # 无界面模式
    chrome_options.add_argument('--headless')
    # 禁用JavaScript
    chrome_options.add_argument("--disable-javascript")
    # 创建 ChromeDriver 实例
    driver = webdriver.Chrome(chromedriver_path, options=chrome_options)
    return driver

# 函数式编程 自动关闭资源
def web_action(func:Callable[[WebDriver], None]):
    try:
        driver = web_driver()
        func(driver)
    finally:
        # 关闭 ChromeDriver
        print("关闭浏览器...")
        driver.quit()


def write_to_excel(file_path: str, data: list[list]):
    # 创建一个新的工作簿
    workbook = openpyxl.Workbook()

    # 获取默认的工作表
    sheet = workbook.active

    # 写入数据到工作表
    for row in data:
        sheet.append(row)

    # 保存工作簿到指定的文件路径
    workbook.save(file_path)

    print(f"数据已写入Excel文件 {file_path}")
    
def find_element(el:WebElement, by=By.ID, value=None) -> WebElement:
    try:
       return el.find_element(by, value)
    except NoSuchElementException:
        return None
    
def top_250(driver:WebDriver):
    
    datas = []
    datas.append(["标题", "作者", "评分", "引述"])
    
    for i in range(0, 10):
        url = 'https://book.douban.com/top250?start=' + str(i)
        print(url)
        driver.get(url)
        els = driver.find_elements(By.CSS_SELECTOR, '#content > div > div.article > div > table > tbody > tr')
        for el in els:
            # 标题
            e_title = find_element(el, By.CSS_SELECTOR, 'div.pl2 > a')
            # 作者
            e_author = find_element(el, By.CSS_SELECTOR, 'p.pl')
            # 评分
            e_star = find_element(el, By.CSS_SELECTOR, 'div.star.clearfix')
            # 引述
            e_quote = find_element(el, By.CSS_SELECTOR, 'p.quote > span')
            print(e_title.text, e_author.text, e_star.text, e_quote.text if e_quote else '')
            datas.append([e_title.text, e_author.text, e_star.text, e_quote.text if e_quote else ''])
        time.sleep(random.randint(2,6))
        
    write_to_excel("豆瓣top250.xlsx", datas)


if __name__ == '__main__':
    web_action(top_250)
    
    
