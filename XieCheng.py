from selenium import webdriver

from PlaceDispatch import PlaceDispatch

option = webdriver.ChromeOptions()
option.add_argument('headless')  # 静默模式
driver = webdriver.Chrome(options=option)
country_base_url = 'https://you.ctrip.com/countrysightlist/China110000/'
place_dispatch = PlaceDispatch(country_base_url=country_base_url)
place_dispatch.dispatch()
driver.quit()
