#-*-coding:utf-8-*-
from selenium import webdriver

from TxtDispatch import TxtDispatch


class ScenicDispatch:
    def __init__(self, scenic_base_url):
        option = webdriver.ChromeOptions()
        option.add_argument('headless')  # 静默模式
        self.browser = webdriver.Chrome(options=option)
        self.scenic_base_url = scenic_base_url

    @staticmethod
    def get_xie_chen_scenic_name(scenic_obj):
        information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
        dl = information.find_element_by_tag_name("dl")
        dt = dl.find_element_by_tag_name("dt")
        a = dt.find_element_by_tag_name("a")
        return a.text

    @staticmethod
    def get_xie_chen_scenic_link(scenic_obj):
        information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
        dl = information.find_element_by_tag_name("dl")
        dt = dl.find_element_by_tag_name("dt")
        a = dt.find_element_by_tag_name("a")
        return a.get_attribute("href")

    @staticmethod
    def get_xie_chen_scenic_address(scenic_obj):
        information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
        dl = information.find_element_by_tag_name("dl")
        dd = dl.find_element_by_tag_name("dd")
        return dd.text

    def get_xie_chen_scenic_page_num(self, browser, scenic_base_url):
        # 景区列表页面
        browser.get(scenic_base_url)
        numpage = self.browser.find_element_by_css_selector("b.numpage")
        return numpage.text

    def dispatch(self):
        total_page = int(self.get_xie_chen_scenic_page_num(self.browser, self.scenic_base_url))
        print("景区总页面数量： " + str(total_page))

        for i in range(1, total_page + 1):
            try:
                page_url = self.scenic_base_url.replace(".html", "/s0-p" + str(i) + ".html")
                self.browser.get(page_url)
                scenic_list = self.browser.find_elements_by_css_selector('div.list_mod2')
                for scenic in scenic_list:
                    print("name: " + self.get_xie_chen_scenic_name(scenic))
                    print("address: " + self.get_xie_chen_scenic_address(scenic))
                    link = self.get_xie_chen_scenic_link(scenic)
                    print("link: " + link)
                    print("-----------------------------")
                    comment_dispatch = TxtDispatch(base_url=link)
                    comment_dispatch.dispatch()
            except Exception as e:
                print(e)
        self.browser.quit()
