import time
from selenium import webdriver


dr = webdriver.Chrome()

dr.get('http://stackoverflow.com/')
dr.execute_script("$(window.open('http://www.google.com/'))")
dr.execute_script("$(window.open('http://facebook.com/'))")

time.sleep(5)
dr.close()
dr.switch_to.window(dr.window_handles[-1])
dr.close()
dr.switch_to.window(dr.window_handles[-1])
dr.close()