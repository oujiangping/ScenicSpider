#-*-coding:utf-8-*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
import os


class TxtDispatch:
    def __init__(self, base_url, timeout=5):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 静默模式
        self.browser = webdriver.Chrome(options=option)
        self.base_url = base_url
        self.current_page = 1
        self.timeout = timeout
        self.txt = None
        time.sleep(1)

    def click_next_comment_page(self):
        try:
            self.current_page += 1
            page_bt_css = "li.ant-pagination-item.ant-pagination-item-" + str(self.current_page)
            page_bt = self.browser.find_element_by_css_selector(page_bt_css)
            self.browser.execute_script("arguments[0].scrollIntoView(false);", page_bt)
            page_bt.click()
            time.sleep(0.5)
            return True
        except Exception as e:
            print(e)
            return False
        return False

    def wait_element_by_css(self, css_selector):
        WebDriverWait(self.browser, self.timeout).until(
            visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def get_comment_list(self):
        self.wait_element_by_css("div.commentDetail")
        comment_list = self.browser.find_elements_by_css_selector("div.commentItem")
        for comment_item in comment_list:
            comment_info = comment_item.find_element_by_css_selector("div.commentDetail")
            average_score = comment_item.find_element_by_css_selector("span.averageScore")
            print("评价： " + comment_info.text)
            print("评分： " + average_score.text)
            if len(average_score.text) > 0:
                if self.txt is None:
                    if not os.path.exists('txt'):
                        os.makedirs('txt')
                    self.wait_element_by_css("span.districtName")
                    district_name_item = self.browser.find_element_by_css_selector("span.districtName")
                    district_name = district_name_item.text
                    self.txt = open('txt/' + district_name + '.txt', mode='w', encoding='utf-8')
                score = average_score.text[:1]
                comment = comment_info.text
                if score.isdigit():
                    if self.txt is not None:
                        self.txt.write(score + '\t' + comment + '\n')
        return comment_list

    def dispatch(self):
        self.browser.get(self.base_url)
        comment_list = self.get_comment_list()
        try:
            while len(comment_list) > 0 and self.click_next_comment_page():
                try:
                    comment_list = self.get_comment_list()
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
        self.browser.quit()
        if self.txt is not None:
            self.txt.close()
