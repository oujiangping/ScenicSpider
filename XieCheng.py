from selenium import webdriver
import time

driver = webdriver.Chrome()
# 景区列表页面
driver.get('https://you.ctrip.com/sight/guiyang33.html')
scenic_list = driver.find_elements_by_css_selector('div.list_mod2')


def get_xie_chen_scenic_name(scenic_obj):
    information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
    dl = information.find_element_by_tag_name("dl")
    dt = dl.find_element_by_tag_name("dt")
    a = dt.find_element_by_tag_name("a")
    return a.text


def get_xie_chen_scenic_link(scenic_obj):
    information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
    dl = information.find_element_by_tag_name("dl")
    dt = dl.find_element_by_tag_name("dt")
    a = dt.find_element_by_tag_name("a")
    return a.get_attribute("href")


def get_xie_chen_scenic_address(scenic_obj):
    information = scenic_obj.find_element_by_css_selector("div.rdetailbox")
    dl = information.find_element_by_tag_name("dl")
    dd = dl.find_element_by_tag_name("dd")
    return dd.text


def get_xie_chen_page_num():
    numpage = driver.find_element_by_css_selector("b.numpage")
    return numpage.text


print("总页面数量： " + get_xie_chen_page_num())

for scenic in scenic_list:
    print("name: " + get_xie_chen_scenic_name(scenic))
    print("address: " + get_xie_chen_scenic_address(scenic))
    print("link: " + get_xie_chen_scenic_link(scenic))
    print("-----------------------------")


time.sleep(200)
driver.quit()