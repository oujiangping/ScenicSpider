from selenium import webdriver
from ScenicDispatch import ScenicDispatch

class PlaceDispatch:
    def __init__(self, country_base_url, driver):
        self.country_base_url = country_base_url
        self.driver = driver

    def get_xie_chen_place_page_num(self):
        country_first_page_url = self.country_base_url + "p1.html"
        # 景区列表页面
        self.driver.get(country_first_page_url)
        numpage = self.driver.find_element_by_css_selector("b.numpage")
        return numpage.text

    def get_xie_chen_place_link(self, place_obj):
        dl = place_obj.find_element_by_tag_name("dl")
        dt = dl.find_element_by_tag_name("dt")
        a = dt.find_element_by_tag_name("a")
        return a.get_attribute("href")

    def get_xie_chen_place_name(self, place_obj):
        dl = place_obj.find_element_by_tag_name("dl")
        dt = dl.find_element_by_tag_name("dt")
        a = dt.find_element_by_tag_name("a")
        return a.text

    def dispatch(self):
        total_page = int(self.get_xie_chen_place_page_num())
        print("地区总页面数量： " + str(total_page))

        for i in range(1, total_page + 1):
            page_url = self.country_base_url + "p" + str(i) + ".html"
            self.driver.get(page_url)
            place_list = self.driver.find_elements_by_css_selector('div.list_mod1')
            for place in place_list:
                place_name = self.get_xie_chen_place_name(place)
                place_link = self.get_xie_chen_place_link(place)
                print("目的地名称: " + place_name)
                print("目的地地址: " + place_link)
                scenic_dispatch = ScenicDispatch(browser=self.driver, scenic_base_url=place_link.replace("place", "sight"))
                scenic_dispatch.dispatch()