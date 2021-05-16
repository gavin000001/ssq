# -*- coding:utf-8 -*-

'''
@FileName : seleniumTest.py
@Time     : 2021/5/15 15:08
@Author: gavin
'''
import unittest
# import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome(executable_path="/Users/zhang/Downloads/chromedriver")  # Chrome浏览器

    def test_search_in_python_org(self):
        driver = self.driver
        # driver.get("https://cn.bing.com/")
        # sb_form_q = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
        # sb_form_q = driver.find_element_by_id('sb_form_q')
        # sb_form_q.send_keys("hello world")
        # # sb_form_q.send_keys(Keys.RETURN)
        # sb_form_q.send_keys(Keys.ENTER)
        driver.get("http://datachart.500.com/ssq/history/history.shtml")
        start = driver.find_element_by_id("start")
        start.clear()
        start.send_keys("03001")
        print(f'已输入 03001')
        # time.sleep(20 * 1000)
        print(f"{driver.title = }")
        self.assertIn("双色球历史数据", driver.title)
        button = driver.find_element_by_xpath('//*[@id="container"]/div/table/tbody/tr[1]/td/div/div[1]/div/table/tbody/tr/td[2]/img')
        # button.send_keys(Keys.RETURN)
        button.send_keys(Keys.ENTER)
        print(f'回车了')
        tdata = driver.find_element_by_id("tdata")
        print(f"{driver.current_url = }")
        print(f"{driver.title = }")
        rows = tdata.text.split("\n")
        for row in rows:
            print(f"{row = }")
        # hrefs = driver.find_elements_by_xpath('/html/body/div[7]/div/ul/li/h2/a')
        # for h in hrefs:
        #     print(f"{h.text = }")
        #     h.send_keys(Keys.ENTER)
        # assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

# https://chromedriver.storage.googleapis.com/index.html?path=90.0.4430.24/
# def main():
#     # url = "http://www.baidu.com"
#     # url = "http://www.python.org"
#     url = "http://datachart.500.com/ssq/history/history.shtml"
#     print 'url =>> ', url
#     # print (f'{url =}>> ')
#     # driver = webdriver.Firefox()  # Firefox浏览器
#     # driver = webdriver.Firefox("驱动路径")
#
#     driver = webdriver.Chrome(executable_path="/Users/zhang/Downloads/chromedriver")  # Chrome浏览器
#     # driver = webdriver.Chrome(executable_path="chromedriver_mac64.zip")  # Chrome浏览器
#
#     # driver = webdriver.Ie()  # Internet Explorer浏览器
#     # driver = webdriver.Edge()  # Edge浏览器
#     # driver = webdriver.Opera()  # Opera浏览器
#     # driver = webdriver.PhantomJS()  # PhantomJS
#
#     # 打开网页
#     driver.get(url)  # 打开url网页 比如 driver.get("http://www.baidu.com")
#     print 'driver.title ==> ', driver.title
#     # assert "Python" in driver.title
#     elem = driver.find_element_by_name("start")
#     elem.send_keys("03001")
#     elem.send_keys(Keys.RETURN)
#     assert "No results found." not in driver.page_source
#     driver.close()


if __name__ == '__main__':
    # main()
    unittest.main()
