import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of, visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait


class CommentDispatch:
    def __init__(self, base_url, timeout=5):
        self.browser = webdriver.Chrome()
        self.base_url = base_url
        self.current_page = 1
        self.timeout = timeout

    def click_next_comment_page(self):
        try:
            self.current_page += 1
            page_bt_css = "li.ant-pagination-item.ant-pagination-item-" + str(self.current_page)
            page_bt = self.browser.find_element_by_css_selector(page_bt_css)
            self.browser.execute_script("arguments[0].scrollIntoView(false);", page_bt)
            page_bt.click()
            time.sleep(0.2)
            return True
        except:
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
        return comment_list

    def dispatch(self):
        self.browser.get(self.base_url)
        comment_list = self.get_comment_list()
        while len(comment_list) > 0 and self.click_next_comment_page():
            comment_list = self.get_comment_list()
        self.browser.quit()
