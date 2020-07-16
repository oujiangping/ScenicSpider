from selenium import webdriver

from PlaceDispatch import PlaceDispatch

driver = webdriver.Chrome()
country_base_url = 'https://you.ctrip.com/countrysightlist/China110000/'
place_dispatch = PlaceDispatch(country_base_url=country_base_url, driver=driver)
place_dispatch.dispatch()
driver.quit()
